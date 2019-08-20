import sys
from antlr4 import *
from LambdaCalculusLexer import LambdaCalculusLexer
from LambdaCalculusParser import LambdaCalculusParser
from LambdaCalculusListener import LambdaCalculusListener
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

def main():
    bracket_checker = BracketCheck()

    visitor_selection = input("Call by value, name or alpha reduce? ")

    expression = input("Enter test expression: ")
    matched_brackets = bracket_checker.check_brackets(expression)

    while matched_brackets == False:
        expression = input("Sorry, mismatched brackets, check and try again?\n")
        matched_brackets = bracket_checker.check_brackets(expression)

    visitor = None
    if visitor_selection == "v":
        visitor = CallByValueVisitor()
    elif visitor_selection == "n":
        visitor = CallByNameVisitor()
    elif visitor_selection == "a":
        #Types are not supported with alpha conversion, so remove all types the user has input before processing
        expression = remove_types(expression)
        visitor = AlphaConversionVisitor()
    else:
        print("No visitor")
    
    if visitor_selection == "v" or visitor_selection == "n":
        #result, return_type, valid_type = run(expression, visitor)
        return_value = run(expression, visitor)
        #if isinstance(return_value,int):
        if return_value == -1:
            print("Syntax error - check the term and try again?")
        elif return_value == -2:
            print("Normal form cannot be found - does this term have a normal form?")
        elif return_value == -5:
            print("Invalid visitor selected - try refreshing the page and try again")
        elif return_value == -6:
            print("Sorry, something went wrong, try entering the term again?")
        else:
            result = return_value[0]
            return_type = return_value[1]
            valid_type = return_value[2]
            result,return_type = post_process(result, return_type)

            arithmetically_reduced = delta_reduction(result)
        
            print("Result = "+result)
            print("Arithmetically reduced = "+arithmetically_reduced)
            print("Return type = "+return_type)
            print("Valid type = "+valid_type)
    elif visitor_selection == "a":
        return_value = run(expression, visitor)
        if return_value == -1:
            print("Syntax error - check the term and try again?")
        else:
            print("Returned alpha = "+return_value)

def web_interface(expression, evaluate_selection):

    session_object = LambdaSessionInformationObject()
    session_object.set_input_term(expression)

    bracket_checker = BracketCheck()
    matched_brackets = bracket_checker.check_brackets(expression)
    if matched_brackets == False:
        return "Mismatched brackets - check the term and try again?","none","none"

    result = None
    return_type = None
    valid_type = None

    if evaluate_selection == "v":
        visitor = CallByValueVisitor(session_object)
    elif evaluate_selection == "n":
        visitor = CallByNameVisitor(session_object)
    elif evaluate_selection == "a":
        expression = remove_types(expression)
        visitor = AlphaConversionVisitor()
    else:
        return -5,"none","none"
    
    return_value = run(expression, visitor)
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
        result,return_type = post_process(result, return_type)

        arithmetically_reduced = delta_reduction(result)

        output_string = "Result = "+str(result)
        if result != arithmetically_reduced:
            output_string = output_string + " = "+str(arithmetically_reduced)+" by arithmetic reduction"
        output_string = output_string + " <a href=\"/more_information\" target=\"_blank\"><span class=\"pale-link\">(click here for evaluation details)</span></a>"
        output_string = output_string + "<br>Valid typing = "+str(valid_type)
        if valid_type == False or valid_type == "False":
            output_string = output_string+"<br>"
            return output_string,session_object.get_typing_context(),session_object.get_beta_steps()
        else:
            output_string = output_string + " under typing context <a href=\"/more_information\" target=\"_blank\"><span class=\"pale-link\">(click here)</span></a><br>"
            output_string = output_string + "Type returned = "+str(return_type)+"<br>"
            return output_string,session_object.get_typing_context(),session_object.get_beta_steps()

def pre_process(expression):
    expression_list = list(expression)
    for i,char in enumerate(expression_list):
        if char == 'λ':
            expression_list[i] = '%'
    
    processed_expression = "".join(expression_list)
    
    return processed_expression

def remove_types(output):
    bad_strings = [":int",":Int",":INT",":bool",":Bool",":BOOL",":None",":NONE",":none"]

    output = str(output)
    for string in bad_strings:
        output = output.replace(string,"")
    
    return output

def post_process(output, return_type=None):
    
    output = str(output)
    return_type = str(return_type)

    output = remove_types(output)

    output_list = list(output)
    for i,character in enumerate(output_list):
        if character == '%':
            output_list[i] = 'λ'
        
    output_processed = "".join(output_list)

    return output_processed,return_type

def run(expression, visitor):
    sys.setrecursionlimit(200)

    expression = pre_process(expression)

    stream = InputStream(expression)
    lexer = LambdaCalculusLexer(stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(LambdaErrorListener())
    try:
        tokens = CommonTokenStream(lexer)
        parser = LambdaCalculusParser(tokens)
        parser.addErrorListener(LambdaErrorListener())
        try:
            tree = parser.term()
            if tree == -2 or tree == -1:
                return tree
            if visitor != None:
                return_value = visitor.visit(tree)
                if return_value == -1:
                    return -1
                elif isinstance(return_value, str):
                    return return_value
                else:
                    result = return_value[0]
                    return_type = return_value[1]
                    valid_type = return_value[2]
                    result,return_type = post_process(result, return_type)

                return str(result),str(return_type),str(valid_type)
            else:
                return -5
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

def delta_reduction(expression):
    expression = pre_process(expression)
    stream = InputStream(expression)
    lexer = LambdaCalculusLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = LambdaCalculusParser(tokens)
    tree = parser.term()
    visitor = DeltaReductionVisitor()
    arithmetically_reduced = visitor.visit(tree)
    arithmetically_reduced,_ = post_process(arithmetically_reduced)

    return arithmetically_reduced

if __name__ == '__main__':
    main()
    # expression = input("Test expression = ")
    # result = delta_reduction(expression)
    # print("Result = "+result)