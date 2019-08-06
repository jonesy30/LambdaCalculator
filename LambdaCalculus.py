import sys
from antlr4 import *
from LambdaCalculusLexer import LambdaCalculusLexer
from LambdaCalculusParser import LambdaCalculusParser
from LambdaCalculusListener import LambdaCalculusListener
from LambdaCalculusVisitor import LambdaCalculusVisitor
from BracketCheck import BracketCheck
from CaseCheck import CaseCheck
from CallByValueVisitor import CallByValueVisitor
from CallByNameVisitor import CallByNameVisitor
from Stack import Stack

from sympy.solvers import solve
from sympy import Symbol

def main():
    bracket_checker = BracketCheck()
    #case_checker = CaseCheck()

    visitor_selection = input("Call by value or call by name? ")

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
    else:
        print("No visitor")
    
    result, return_type, valid_type = run(expression, visitor)
    print("Result = "+result)
    print("Return type = "+return_type)
    print("Valid type = "+valid_type)

def web_interface(expression, evaluate_selection):

    result = None
    return_type = None
    valid_type = None

    if evaluate_selection == "v":
        visitor = CallByValueVisitor()
        result, return_type, valid_type = run(expression, visitor)
    elif evaluate_selection == "n":
        visitor = CallByNameVisitor()
        result, return_type, valid_type = run(expression, visitor)
    elif evaluate_selection == "a":
        #I should be running the alpha conversion code here
        return -1
    else:
        return -1
    
    return str(result), str(return_type), str(valid_type)

def run(expression, visitor):
    stream = InputStream(expression)
    lexer = LambdaCalculusLexer(stream)
    #lexer = LambdaCalculusLexer(StdinStream())
    tokens = CommonTokenStream(lexer)
    parser = LambdaCalculusParser(tokens)
    tree = parser.term()
    if visitor != None:
        result,return_type,valid_type = visitor.visit(tree)
        result,return_type = visitor.post_process(result, return_type)
        
        return str(result),str(return_type),str(valid_type)
    else:
        return -1


if __name__ == '__main__':
    main()