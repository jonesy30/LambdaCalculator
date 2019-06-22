import sys
from sys import argv
from antlr4 import *
from arithmeticLexer import arithmeticLexer
from arithmeticParser import arithmeticParser

def handleExpression(expr):
    adding = True
    value = 0
    for child in expr.getChildren():
        if isinstance(child, tree.Tree.TerminalNode):
            adding = child.getText() == "+"
        else:
            multValue = handleMultiply(child)
            if adding:
                value += multValue
            else:
                value -= multValue

    print("Parsed expression " + expr.getText() + " has value " + str(value))

def handleMultiply(expr):
    multiplying = True
    value = 1
    for child in expr.getChildren():
        if isinstance(child, tree.Tree.TerminalNode):
            multiplying = child.getText() == "*"
        else:
            if multiplying:
                value *= int(child.getText())
            else:
                value /= int(child.getText())
        
    return value

def main(self):
    lexer = arithmeticLexer(StdinStream())
    #lexer = arithmeticLexer(FileStream(argv[1]))
    #lexer = arithmeticLexer(str(sys.argv[1]))
    stream = CommonTokenStream(lexer)
    parser = arithmeticParser(stream)
    tree = parser.expression()
    handleExpression(tree)

if __name__ == '__main__':
    main(sys.argv)
