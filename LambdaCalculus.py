import sys
from antlr4 import *
from LambdaCalculusLexer import LambdaCalculusLexer
from LambdaCalculusParser import LambdaCalculusParser
from LambdaCalculusListener import LambdaCalculusListener
from LambdaCalculusVisitor import LambdaCalculusVisitor
from AlphaCalculator import calculate_alpha
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
    expression = calculate_alpha()
    stream = InputStream(expression)
    lexer = LambdaCalculusLexer(stream)
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