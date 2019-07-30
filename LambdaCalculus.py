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
    case_checker = CaseCheck()

    expression = input("Enter test expression: ")
    matched_brackets = bracket_checker.check_brackets(expression)

    while matched_brackets == False:
        expression = input("Sorry, mismatched brackets, check and try again?\n")
        matched_brackets = bracket_checker.check_brackets(expression)

    #NOTE: I do not allow any lowercase values
    all_lowercase = case_checker.check_case(expression)
    while all_lowercase == False:
        expression = input("Sorry, no uppercase values allowed, please rewrite and try again?\n")
        all_lowercase = case_checker.check_case(expression)

    stream = InputStream(expression)
    lexer = LambdaCalculusLexer(stream)
    #lexer = LambdaCalculusLexer(StdinStream())
    tokens = CommonTokenStream(lexer)
    parser = LambdaCalculusParser(tokens)
    tree = parser.term()
    visitor = CallByValueVisitor()
    #visitor = CallByNameVisitor()
    result,return_type,valid_type = visitor.visit(tree)
    print("Result = "+str(result))
    print("Return type = "+str(return_type))
    print("Valid type = "+str(valid_type))
    #printer = Listener()
    #walker = ParseTreeWalker()
    #walker.walk(printer, tree)

if __name__ == '__main__':
    main()