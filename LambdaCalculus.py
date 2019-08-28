import sys
from antlr4 import *
from LambdaCalculusLexer import LambdaCalculusLexer
from LambdaCalculusParser import LambdaCalculusParser
from LambdaCalculusVisitor import LambdaCalculusVisitor
from LambdaErrorListener import LambdaErrorListener, SyntaxTokenError
from BracketCheck import BracketCheck
from CallByValueVisitor import CallByValueVisitor
from CallByNameVisitor import CallByNameVisitor
from AlphaConversionVisitor import AlphaConversionVisitor
from DeltaReductionVisitor import DeltaReductionVisitor
from LambdaSessionInformationObject import LambdaSessionInformationObject
from Stack import Stack

from sympy.solvers import solve
from sympy import Symbol

#The main runner for the lambda calculus evaluator code connects all other classes into the appropriate methods

#Method which is called if the code is run via the command line
def main():
    bracket_checker = BracketCheck()

    #Get the evaluator to be used to evaluate the lambda term
    visitor_selection = input("Call by value, name or alpha reduce? ")

    #Get the input lambda term
    expression = input("Enter expression: ")

    #Check whether the brackets are valid or not (all open brackets closed, no stray close brackets)
    #Continually get the user to re-enter until the brackets are valid
    matched_brackets = bracket_checker.check_brackets(expression)
    while matched_brackets == False:
        expression = input("Sorry, mismatched brackets, check and try again?\n")
        matched_brackets = bracket_checker.check_brackets(expression)

    #Session object used to store information about the current lambda term's processing
    session_object = LambdaSessionInformationObject()
    session_object.set_input_term(expression)

    #Get the visitor in accordance with the evaluation method the user has selected
    visitor = None
    if visitor_selection == "v":
        visitor = CallByValueVisitor(session_object)
    elif visitor_selection == "n":
        visitor = CallByNameVisitor(session_object)
    elif visitor_selection == "a":
        #Types are not supported with alpha conversion, so remove all types the user has input before processing
        expression = remove_types(expression)
        visitor = AlphaConversionVisitor()
    else:
        print("No visitor")
    
    #With call by name and call by value, the output has a return type and a type validity
    #Unpack these from the output
    if visitor_selection == "v" or visitor_selection == "n":
        #Perform the beta-reduction
        return_value = run(expression, visitor)

        #Process the error and display the appropriate result if an error is returned
        if return_value == -1:
            print("Syntax error - check the term and try again?")
        elif return_value == -2:
            print("Normal form cannot be found - does this term have a normal form?")
        elif return_value == -5:
            print("Invalid visitor selected - try refreshing the page and try again")
        elif return_value == -6:
            print("Sorry, something went wrong, try entering the term again?")
        else:
            #If there is no error, get the return-type, the type-validity and the result of the expression
            result = return_value[0]
            return_type = return_value[1]
            valid_type = return_value[2]

            #Remove the types from the term and convert all % to a lambda symbol
            result,return_type = post_process(result, return_type)

            #Arithmetically evaluate the resultant term, and post-process the result again
            arithmetically_reduced = delta_reduction(result)
            arithmetically_reduced,_ = post_process(arithmetically_reduced)
        
            #Print the results to the command line
            print("Result = "+result)
            print("Arithmetically reduced = "+arithmetically_reduced)
            print("Return type = "+return_type)
            print("Valid type = "+valid_type)
    elif visitor_selection == "a":
        #Perform the alpha-reduction
        return_value = run(expression, visitor)
        #Return an error message if there is a syntax error, the alpha converted term if processing was successful
        if return_value == -1:
            print("Syntax error - check the term and try again?")
        else:
            print("Returned alpha = "+return_value)

#Method which is called by the web interface, with the input lambda term and the evaluation method selection incoming
def run_lambda_calculator(expression, evaluate_selection):

    #Create a new session object (designed to help share information between webpages)
    session_object = LambdaSessionInformationObject()
    session_object.set_input_term(expression)

    #Make sure the brackets are valid (all open brackets are closed, there are no stray close brackets)
    bracket_checker = BracketCheck()
    matched_brackets = bracket_checker.check_brackets(expression)
    if matched_brackets == False:
        #Return an error message if brackets are mismatched
        return "Mismatched brackets - check the term and try again?","none","none"

    #Initialise resultant variables
    result = None
    return_type = None
    valid_type = None

    #Create the visitor object depending on the user selection
    if evaluate_selection == "v":
        visitor = CallByValueVisitor(session_object)
    elif evaluate_selection == "n":
        visitor = CallByNameVisitor(session_object)
    elif evaluate_selection == "a":
        #Types are not supported with alpha conversion so remove any types in the term
        expression = remove_types(expression)
        visitor = AlphaConversionVisitor()
    else:
        #If there is no visitor, return the appropriate error code
        return "Invalid visitor selected - try refreshing the page and try again",-1,-1
    
    #Run the lambda evaluation using the selected visitor and return the result
    return_value = run(expression, visitor)

    #Print the appropriate error message if an error message is returned
    if return_value == -1:
        return "Syntax error - check the term and try again?",-1,-1
    elif return_value == -2:
        return "Normal form cannot be found - does this term have a normal form?",-1,-1
    elif return_value == -5:
        return "Invalid visitor selected - try refreshing the page and try again",-1,-1
    elif return_value == -6:
        return "Sorry, something went wrong, try entering the term again?",-1,-1
    elif evaluate_selection == "a":
        #If alpha conversion is selected, just post-process and return result
        return_value,_ = post_process(return_value)
        return "Result = "+return_value,"none","none"
    else:
        #If non-alpha conversion visitor selected, variable needs to be unpacked and delta-reduced
        result = return_value[0]
        return_type = return_value[1]
        valid_type = return_value[2]

        #Remove types from the final term and convert % back to a lambda symbol
        result,return_type = post_process(result, return_type)

        #Perform the arithmetic evaluation and process again
        arithmetically_reduced = delta_reduction(result)
        arithmetically_reduced,_ = post_process(arithmetically_reduced)

        #Build up the output which is to be given to the web interface
        output_string = "Result = "+str(result)

        #If arithmetic reduction did something, add this to the output, else just leave as it is
        if result != arithmetically_reduced:
            output_string = output_string + " = "+str(arithmetically_reduced)+" by arithmetic reduction"
        #Add the link to the more information page when there is beta-reduction steps to give
        output_string = output_string + " <a href=\"/more_information\" target=\"_blank\"><span class=\"pale-link\">(click here for evaluation details)</span></a>"
        #Set up the heading for the valid_typing output
        output_string = output_string + "<br>Valid typing = "+str(valid_type)
        #If the typing is invalid, don't show the type returned, just return here
        if valid_type == False or valid_type == "False":
            output_string = output_string+"<br>"
            return output_string,session_object.get_typing_context(),session_object.get_beta_steps()
        #If the typing is valid, return this, the type returned and a link to get to the typing context page
        else:
            output_string = output_string + " under typing context <a href=\"/more_information\" target=\"_blank\"><span class=\"pale-link\">(click here)</span></a><br>"
            output_string = output_string + "Type returned = "+str(return_type)+"<br>"
            return output_string,session_object.get_typing_context(),session_object.get_beta_steps()

#Method which is called by the unit tests with the incoming lambda term and the evaluation method selection
def unit_t_interface(expression, evaluate_selection):

    #Create the session object to store information about the term being processed
    session_object = LambdaSessionInformationObject()
    session_object.set_input_term(expression)

    #Make sure the brackets are valid (all open brackets are closed, there are no stray close brackets)    
    bracket_checker = BracketCheck()
    matched_brackets = bracket_checker.check_brackets(expression)
    if matched_brackets == False:
        return "Mismatched brackets - check the term and try again?"

    result = None
    return_type = None
    valid_type = None

    #Get the required visitor based on the selection made
    if evaluate_selection == "v":
        visitor = CallByValueVisitor(session_object)
    elif evaluate_selection == "n":
        visitor = CallByNameVisitor(session_object)
    elif evaluate_selection == "a":
        #Types are not supported with alpha conversion so remove any types in the term
        expression = remove_types(expression)
        visitor = AlphaConversionVisitor()
    else:
        #If an invalid visitor is selected, return the appropriate error message
        return "Invalid visitor selected - try refreshing the page and try again"
    
    #Run the evaluation with the incoming lambda term and the selected visitor
    return_value = run(expression, visitor)

    #Print the appropriate error message if an error message is returned
    if return_value == -1:
        return "Syntax error - check the term and try again?"
    elif return_value == -2:
        return "Normal form cannot be found - does this term have a normal form?"
    elif return_value == -5:
        return "Invalid visitor selected - try refreshing the page and try again"
    elif return_value == -6:
        return "Sorry, something went wrong, try entering the term again?"
    elif evaluate_selection == "a":
        #If alpha conversion is selected, just post-process and return result
        return return_value
    else:
        #If non-alpha conversion visitor selected, variable needs to be unpacked and delta-reduced
        result = return_value[0]
        return_type = return_value[1]
        valid_type = return_value[2]

        #Perform the delta reduction and return the result
        arithmetically_reduced = delta_reduction(result)
        return arithmetically_reduced,valid_type,return_type

#Convert all lambda symbols (coming from the web-interface) to a % which is used by the underlying lambda code
def pre_process(expression):

    #Make the expression into a list (so elements can be accessed and modified by index)
    expression_list = list(expression)
    for i,char in enumerate(expression_list):
        if char == 'λ':
            expression_list[i] = '%'
    
    #Create a string from the resultant list and return it
    processed_expression = "".join(expression_list)
    return processed_expression

#Function which removes all types from the output term (since this is covered by the typing context and the final type)
def remove_types(output):
    bad_strings = [":int",":Int",":INT",":bool",":Bool",":BOOL",":None",":NONE",":none"]

    #Replace all types with no character (deleting them)
    output = str(output)
    for string in bad_strings:
        output = output.replace(string,"")
    
    return output

#Method which takes all % symbols (used throughout lambda processing for simplicity) and converts them to a lambda symbol
#It also returns any types in the final string since this is covered by the typing context and the final type
def post_process(output, return_type=None):
    
    #Convert the output and the return type to a String
    output = str(output)
    return_type = str(return_type)

    #Remove any types in the final string
    output = remove_types(output)

    #Change each % to a lambda symbol
    output_list = list(output)
    for i,character in enumerate(output_list):
        if character == '%':
            output_list[i] = 'λ'
        
    #Convert the created list to a string, and return the result 
    output_processed = "".join(output_list)
    return output_processed,return_type

#Function which runs the evaluation using the incoming expression as an input to the selected visitor
def run(expression, visitor):

    #Recursion limit set to protect the code if there is no normal form of a lambda term found -
    #the code will just keep attempting to solve it forever so set a recursion limit which breaks after a set stack depth
    #throwing an error which can be caught with an appropriate error message
    sys.setrecursionlimit(200)

    #Convert all lambda symbols into a % used by the underlying code
    expression = pre_process(expression)

    #Feed the expression through ANTLR generated classes as required by ANTLR
    stream = InputStream(expression)
    #Create the lexer and put the stream through it
    lexer = LambdaCalculusLexer(stream)
    lexer.removeErrorListeners()

    #Add a custom error listener to the lexer which catches errors so they can be dealt with in a more useful way than the program just stopping
    lexer.addErrorListener(LambdaErrorListener())
    try:
        #Create the parser and pass the tokens through it
        tokens = CommonTokenStream(lexer)
        parser = LambdaCalculusParser(tokens)
        #Add a custom error listener to the parser which catches errors so they can be dealt with in a more useful way than the program just stopping
        parser.addErrorListener(LambdaErrorListener())
        try:
            #Tree == -2 is a recursion error, tree == -1 is a syntax error
            tree = parser.term()
            if tree == -2 or tree == -1:
                return tree
            #If the visitor exists, process the tree using the visitor
            if visitor != None:
                return_value = visitor.visit(tree)
                if return_value == -1:
                    return -1
                #If the returned output is a string, return as is, else it needs to be unpacked
                elif isinstance(return_value, str):
                    return return_value
                #If the returned output is not a string, unpack the result into its individual components
                #(result, return type and type validity)
                else:
                    result = return_value[0]
                    return_type = return_value[1]
                    valid_type = return_value[2]

                    #Remove types from the result and convert any % to a lambda symbol
                    result,return_type = post_process(result, return_type)

                return str(result),str(return_type),str(valid_type)
            else:
                #If the visitor does not exist, return -5 error code
                return -5
        #Handle errors by returning the appropriate error code (picked up and processed by the interface method)
        except SyntaxTokenError:
            return -1
        except RecursionError:
            return -2
        #Exceptions can be Syntax errors or something else
        except Exception as e:
            error_message = str(e)
            #If the exception is a SyntaxTokenError raised by antlr
            if "SyntaxTokenError" in error_message:
                return -1
            #Else something else has gone wrong
            else:
                print(error_message)
                return -6
    except SyntaxTokenError:
        return -1
    except RecursionError:
        return -2
    except Exception as e:
        error_message = str(e)
        #If the exception is a SyntaxTokenError raised by antlr
        if "SyntaxTokenError" in error_message:
            return -1
        #Else something else has gone wrong
        else:
            print(error_message)
            return -6

#Method which arithmetically evaluates the resultant term from the user
def delta_reduction(expression):

    #Convert any lamdba symbols to a % symbol for processing
    expression = pre_process(expression)

    #Pass the input expression through the various ANTLR generated classes as required by ANTLR
    stream = InputStream(expression)
    lexer = LambdaCalculusLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = LambdaCalculusParser(tokens)
    tree = parser.term()

    #Pass the resultant tree to the delta reduction visitor for arithmetic evaluation
    visitor = DeltaReductionVisitor()
    arithmetically_reduced = visitor.visit(tree)

    #Return the result of the tree
    return arithmetically_reduced

if __name__ == '__main__':
    main()
    # expression = input("Test expression = ")
    # result = delta_reduction(expression)
    # print("Result = "+result)