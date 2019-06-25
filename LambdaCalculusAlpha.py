import sys
from antlr4 import *
from LambdaCalculusLexer import LambdaCalculusLexer
from LambdaCalculusParser import LambdaCalculusParser
from LambdaCalculusListener import LambdaCalculusListener

from sympy.solvers import solve
from sympy import Symbol

class Listener(LambdaCalculusListener):

    def enterAbstraction(self, expr):
        abstraction = expr.getText()
        print("Abstraction = "+abstraction)

        bound_value = None

        if abstraction[0] == '(':
            abstraction = abstraction[1:]
        if abstraction[-1] == ')':
            abstraction = abstraction[:-1]
        
        if abstraction[0] == '%':
            bound_value = abstraction[1]
        else :
            print("Nothing found!!")
        
        print("Bound value = "+bound_value)
        
        firstDelPos=abstraction.find("(")
        secondDelPos=abstraction.find(")")
        if firstDelPos != None and secondDelPos != None:
            abstraction = abstraction.replace(abstraction[firstDelPos:secondDelPos+1], "")
        print("After bracket checker: "+abstraction)

        abstraction_list = list(abstraction)
        for i,letter in enumerate(abstraction_list):
            if letter.isalpha():
                if letter != bound_value:
                    abstraction_list[i] = letter.upper()
        
        abstraction = "".join(abstraction_list)
        print("New abstraction = "+abstraction)

        #Ok, I still need a way to put this back into the tree (which might be a massive issue but hey, we'll see)
        #and we could maybe always do it in place? not sure

def main():
    lexer = LambdaCalculusLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = LambdaCalculusParser(stream)
    tree = parser.term()
    #handleExpression(tree)
    printer = Listener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()