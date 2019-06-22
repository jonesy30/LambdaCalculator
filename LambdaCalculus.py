import sys
from antlr4 import *
from LambdaCalculusLexer import LambdaCalculusLexer
from LambdaCalculusParser import LambdaCalculusParser
from LambdaCalculusListener import LambdaCalculusListener

from sympy.solvers import solve
from sympy import Symbol

class Listener(LambdaCalculusListener):
    abstraction = None
    value = None
    variable = None
    function = None

    # def enterTerm(self, expr):
    #     if expr.abstraction() is not None:
    #         print("Abstraction: "+ expr.abstraction().getText())
    #     else:
    #         print("Abstraction = none")
    #     if expr.variable() is not None:
    #         print("Variable: " + expr.variable().getText())
    #     else:
    #         print("Variable = none")
    #     if expr.application() is not None:
    #         print("Application: " + expr.application().getText())
    #     else:
    #         print("Application = none")

    def enterApplication(self, expr):
        Listener.abstraction = None
        Listener.value = None
        Listener.variable = None
        Listener.function = None
    
    def exitApplication(self, expr):
        print("Abstraction: "+Listener.abstraction)
        print("Value: "+Listener.value)
        print("Variable: "+Listener.variable)

        Listener.function = Listener.function.replace(Listener.variable,Listener.value)
        print("New function: "+Listener.function)
        print("Evaluation: "+str(eval(Listener.function)))

    def enterAbstraction(self, expr):
        Listener.abstraction = expr.getText()
        print("Entering abstraction: "+Listener.abstraction)

    def enterExpression(self, expr):
        Listener.value = expr.getText()
        print("Entering expression")

    def enterVariable(self, expr):
        Listener.variable = expr.getText()
        print("Entering variable")

    def enterFunction(self, expr):
        Listener.function = expr.getText()
        print("Entering function")

def handleExpression(expr):
    for child in expr.getChildren():
        if isinstance(child, tree.Tree.TerminalNode):
            print("Terminal node at: " + child.getText())
        else:
            print("Not terminal node at: " + child.getText())
            handleExpression(child)
        # print(child.getPayload().getText())
        # if child.getPayload().abstraction() is not None:
        # #if isinstance(child.getPayload(), expr.abstraction()):
        #     print("Abstraction: "+ expr.abstraction().getText())
        # else:
        #     print("Abstraction = none")
        # if child.variable() is not None:
        #     print("Variable: " + expr.variable().getText())
        # else:
        #     print("Variable = none")
        # if child.application() is not None:
        #     print("Application: " + expr.application().getText())
        #     for sub_child in expr.application().getChildren():
        #         print(sub_child.getText())
        # else:
        #     print("Application = none")

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