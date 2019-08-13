import sys
from antlr4 import *
from LambdaCalculusLexer import LambdaCalculusLexer
from LambdaCalculusParser import LambdaCalculusParser
from LambdaCalculusListener import LambdaCalculusListener
from LambdaCalculusVisitor import LambdaCalculusVisitor
from LambdaErrorListener import LambdaErrorListener, SyntaxTokenError
from BracketCheck import BracketCheck
from CaseCheck import CaseCheck
from CallByValueVisitor import CallByValueVisitor
from CallByNameVisitor import CallByNameVisitor
from AlphaConversionVisitor import AlphaConversionVisitor
from DeltaReductionVisitor import DeltaReductionVisitor
from Stack import Stack

from sympy.solvers import solve
from sympy import Symbol

def main():
    bracket_checker = BracketCheck()
    #case_checker = CaseCheck()

    visitor_selection = input("Call by value, name or alpha reduce? ")

    expression = input("Enter test expression: ")
    matched_brackets = bracket_checker.check_brackets(expression)

    while matched_brackets == False:
        expression = input("Sorry, mismatched brackets, check and try again?\n")
        matched_brackets = bracket_checker.check_brackets(expression)

    # #NOTE: I do not allow any uppercase values
    # all_lowercase = case_checker.check_case(expression)
    # while all_lowercase == False:
    #     expression = input("Sorry, no uppercase values allowed, please rewrite and try again?\n")
    #     all_lowercase = case_checker.check_case(expression)

    visitor = None
    if visitor_selection == "v":
        visitor = CallByValueVisitor()
    elif visitor_selection == "n":
        visitor = CallByNameVisitor()
    elif visitor_selection == "a":
        visitor = AlphaConversionVisitor()
    else:
        print("No visitor")
    
    if visitor_selection == "v" or visitor_selection == "n":
        #result, return_type, valid_type = run(expression, visitor)
        return_value = run(expression, visitor)
        if isinstance(return_value,int):
            if return_value == -1:
                print("Syntax error - check the term and try again?")
            elif return_value == -2:
                print("Normal form cannot be found - does this term have a normal form?")
            elif return_value == -5:
                print("Invalid visitor selected - try refreshing the page and try again")
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

    bracket_checker = BracketCheck()
    matched_brackets = bracket_checker.check_brackets(expression)
    if matched_brackets == False:
        return "Mismatched brackets - check the term and try again?"

    result = None
    return_type = None
    valid_type = None

    if evaluate_selection == "v":
        visitor = CallByValueVisitor()
    elif evaluate_selection == "n":
        visitor = CallByNameVisitor()
    elif evaluate_selection == "a":
        visitor = AlphaConversionVisitor()
    else:
        return -5
    
    return_value = run(expression, visitor)
    print("Return value = "+str(return_value))
    if isinstance(return_value,int):
        if return_value == -1:
            return "Syntax error - check the term and try again?"
        elif return_value == -2:
            return "Normal form cannot be found - does this term have a normal form?"
        elif return_value == -5:
            return "Invalid visitor selected - try refreshing the page and try again"
        else:
            return str(return_value)
    elif isinstance(return_value,str):
        return "Result = "+return_value
    else:
        result = return_value[0]
        return_type = return_value[1]
        valid_type = return_value[2]
        result,return_type = post_process(result, return_type)

        arithmetically_reduced = delta_reduction(result)
        if result == arithmetically_reduced:
            return "Result = "+str(result)+"<br>"+"Valid typing = "+str(valid_type)+"<br>"+"Type returned = "+str(return_type)+"<br>"        
    
    return "Result = "+str(result)+" = "+str(arithmetically_reduced)+" by arithmetic reduction<br>"+"Valid typing = "+str(valid_type)+"<br>"+"Type returned = "+str(return_type)+"<br>"

def pre_process(expression):

    expression_list = list(expression)
    for i,char in enumerate(expression_list):
        if char == 'λ':
            expression_list[i] = '%'
    
    processed_expression = "".join(expression_list)
    
    return processed_expression

def post_process(output, return_type=None):

    bad_strings = [":int",":Int",":INT",":bool",":Bool",":BOOL",":None",":NONE",":none"]

    output = str(output)
    return_type = str(return_type)
    for string in bad_strings:
        output = output.replace(string,"")

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
        except RecursionError:
            return -2
        except Exception:
            return -1
    except RecursionError:
        return -2
    except Exception:
        return -1

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