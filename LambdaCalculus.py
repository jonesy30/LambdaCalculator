import sys
from antlr4 import *
from LambdaCalculusLexer import LambdaCalculusLexer
from LambdaCalculusParser import LambdaCalculusParser
from LambdaCalculusListener import LambdaCalculusListener
from LambdaCalculusVisitor import LambdaCalculusVisitor
from BracketCheck import BracketCheck
from CaseCheck import CaseCheck
from MyVisitor import MyVisitor

from sympy.solvers import solve
from sympy import Symbol

#taken from https://www.sanfoundry.com/python-program-implement-stack/
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()

def main():
    #I need to put a bracket checker in here
    bracket_checker = BracketCheck()
    case_checker = CaseCheck()

    expression = input("Enter test expression: ")
    matched_brackets = bracket_checker.check_brackets(expression)

    while matched_brackets == False:
        expression = input("Sorry, mismatched brackets, check and try again?\n")
        matched_brackets = bracket_checker.check_brackets(expression)

    all_lowercase = case_checker.check_case(expression)
    while all_lowercase == False:
        expression = input("Sorry, no uppercase values allowed, please rewrite and try again?\n")
        all_lowercase = case_checker.check_case(expression)

    #expression = calculate_alpha()
    stream = InputStream(expression)
    lexer = LambdaCalculusLexer(stream)
    #lexer = LambdaCalculusLexer(StdinStream())
    tokens = CommonTokenStream(lexer)
    parser = LambdaCalculusParser(tokens)
    tree = parser.term()
    visitor = MyVisitor()
    #visitor = LambdaCalculusVisitor()
    result = visitor.visit(tree)
    print(result)
    #printer = Listener()
    #walker = ParseTreeWalker()
    #walker.walk(printer, tree)

if __name__ == '__main__':
    main()