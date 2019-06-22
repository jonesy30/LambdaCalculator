import sys
from antlr4 import *
from LambdaCalculusLexer import LambdaCalculusLexer
from LambdaCalculusParser import LambdaCalculusParser
from LambdaCalculusListener import LambdaCalculusListener

from sympy.solvers import solve
from sympy import Symbol

#Note to self: I definitely absolutely need a stack

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

class Listener(LambdaCalculusListener):
    abstraction = Stack()
    value = Stack()
    variable = Stack()
    function = Stack()
    solve_for = Stack()

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
    
    def exitApplication(self, expr):
        #print("Abstraction: "+Listener.abstraction)
        #print("Value: "+Listener.value)
        #print("Variable: "+Listener.variable)

        if not Listener.function.is_empty():
            function = Listener.function.pop().replace(Listener.solve_for.pop(),Listener.value.pop())
            print("New function: "+function)
            output_value = str(eval(function))
            print("Evaluated = "+output_value)
            Listener.value.push(output_value) 

    def enterAbstraction(self, expr):
        Listener.abstraction = expr.getText()

    def enterValue_term(self, expr):
        value = expr.getText().split(")")[-1]
        print("Value = "+value)
        Listener.value.push(value)

    def enterFunction(self, expr):
        Listener.function.push(expr.getText())
    
    def enterAbstraction_term(self, expr):
        Listener.solve_for.push(expr.getText().replace('%',''))

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