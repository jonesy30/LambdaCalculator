from MyLambdaVisitor import MyLambdaVisitor
from Stack import Stack
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
else:
    from LambdaCalculusParser import LambdaCalculusParser

class ArithmeticVisitor(MyLambdaVisitor):

    # def handleExpression(self,expr):
    #     adding = True
    #     value = 0

    #     for child in expr.getChildren():
    #         print("Child = "+str(child.getText()))
    #         if isinstance(child, tree.Tree.TerminalNode):
    #             adding = child.getText() == "+"
    #             print("Adding = "+str(adding)+"?")
    #         else:
    #             multValue = self.handleMultiply(child)
    #             if adding:
    #                 value += multValue
    #             else:
    #                 value -= multValue

    #     print("Returning value "+str(value))
    #     return value

    # def handleMultiply(self,expr):
    #     multiplying = True
    #     value = 1
    #     for child in expr.getChildren():
    #         if isinstance(child, tree.Tree.TerminalNode):
    #             multiplying = child.getText() == "*"
    #         else:
    #             if multiplying:
    #                 value *= int(child.getText())
    #             else:
    #                 value /= int(child.getText())
            
    #     return value

    # Visit a parse tree produced by LambdaCalculusParser#function.
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):
        print("In my arithmertic visitor")

        operation = ctx.getChild(1).getText()

        # if isinstance(ctx.getChild(0), tree.Tree.TerminalNode):
        #     adding = child.getText() == "+"
        # else:
        #     multiplying = True
        #     value = 1
        #     if isinstance(child, tree.Tree.TerminalNode):
        #         multiplying = child.getText() == "*"
        #     else:
        #         if multiplying:
        #             value *= int(child.getText())
        #         else:
        #             value /= int(child.getText())
                
        #     if adding:
        #         value += multValue
        #     else:
        #         value -= multValue

        # print("Parsed expression " + expr.getText() + " has value " + str(value))

        result = 0
        if operation == "+" or operation == "-":
            left = self.visit(ctx.getChild(0))
            print("Left = "+str(left))
            right = self.visit(ctx.getChild(2))
            print("Right = "+str(right))
            result = self.evaluate(left, operation, right)
        elif operation == "*" or operation == '/':
            result = self.evaluate(ctx.getChild(0).getText(),operation,ctx.getChild(2).getText())
            left = self.visit(ctx.getChild(0))
            print("Left = "+str(left))
            right = self.visit(ctx.getChild(2))
            print("Right = "+str(right))
        else:
            print("Something else? "+str(operation))

        return result
    
    def evaluate(self,left,operation,right):
        if operation == "+":
            result = int(left) + int(right)
        elif operation == "-":
            result = int(left) - int(right)
        elif operation == "*":
            result = int(left) * int(right)
        elif operation == "/":
            result = int(left) // int(right) #ROUNDING

        return result
    