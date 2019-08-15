from LambdaCalculusVisitor import LambdaCalculusVisitor
from AlphaCalculatorFromComplete import AlphaCalculatorFromComplete
from antlr4 import *
from Stack import Stack
if __name__ is not None and "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
    from .LambdaCalculusLexer import LambdaCalculusLexer
else:
    from LambdaCalculusParser import LambdaCalculusParser
    from LambdaCalculusLexer import LambdaCalculusLexer
import re

class DeltaReductionVisitor(LambdaCalculusVisitor):
    def __init__(self):
        super()

    # Visit a parse tree produced by LambdaCalculusParser#term.
    def visitTerm(self, ctx:LambdaCalculusParser.TermContext):
        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#application.
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()
        else:
            return self.visit(ctx.getChild(0)) + self.visit(ctx.getChild(1))

    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()
        else:
            right_child = self.visit(ctx.getChild(2))
            return ctx.getChild(0).getText() + ctx.getChild(1).getText() + right_child

    # Visit a parse tree produced by LambdaCalculusParser#abstraction_term.
    def visitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        return ctx.getText()

    # Visit a parse tree produced by LambdaCalculusParser#function.
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):

        bool_bool = ["&","|"]
        int_int = ["+","-","*","/","^","==",">","<"]

        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            inner_function = self.visit(ctx.getChild(1))

            #If the inner function is still a function
            for operation in bool_bool:
                if operation in inner_function:
                    return "" + ctx.getChild(0).getText() + inner_function + ctx.getChild(2).getText()
            for operation in int_int:
                if operation in inner_function:
                    return "" + ctx.getChild(0).getText() + inner_function + ctx.getChild(2).getText()
            #If the function reaches this point the inner term is not a function, so safe to remove parentheses
            return inner_function
        else:
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))

            number_regex = "^0|^[1-9][0-9]*$"

            left_number = None
            right_number = None
            if re.match(number_regex, left):
                left_number = left    
            if re.match(number_regex, right):
                right_number = right

            left_bool = None
            right_bool = None

            if left == 'TRUE' or left == 'true' or left == 'True':
                left_bool = True
            elif left == 'FALSE' or left == 'false' or left == 'False':
                left_bool = False
            if right == 'TRUE' or right == 'true' or right == 'True':
                right_bool = True
            elif right == 'FALSE' or right == 'false' or right == 'False':
                right_bool = False

            op = ctx.getChild(1).getText()
            
            remaining_string = None
            if right_number == None and right_bool == None:
                right_left_match = re.search("^0|^[1-9][0-9]*", right)
                if right_left_match!=None and left_number!=None:
                    right_number = right_left_match.group(0)
                    remaining_string = re.sub("^0|^[1-9][0-9]*", "", right, 1)

                right_left_match = re.search("^[Tt][Rr][Uu][Ee]|^[Ff][Aa][Ll][Ss][Ee]", right)
                if right_left_match!=None and left_bool!=None:
                    right_bool = right_left_match.group(0)
                    remaining_string = re.sub("^[Tt][Rr][Uu][Ee]|^[Ff][Aa][Ll][Ss][Ee]", "", right, 1)

            return_string = "" + left + op + right
            if op in int_int:
                if left_number is not None and right_number is not None:
                    if op == "+":
                        arithmetic_returned = int(left_number) + int(right_number)
                    elif op == "-":
                        arithmetic_returned = int(left_number) - int(right_number)
                    elif op == "*":
                        arithmetic_returned = int(left_number) * int(right_number)
                    elif op == "/":
                        arithmetic_returned = int(left_number) // int(right_number)
                    elif op == "^":
                        arithmetic_returned = int(left_number) ** int(right_number)
                    elif op == "==":
                        arithmetic_returned = int(left_number) == int(right_number)
                    elif op == ">":
                        arithmetic_returned = int(left_number) > int(right_number)
                    elif op == "<":
                        arithmetic_returned = int(left_number) < int(right_number)
                    else: 
                        arithmetic_returned = return_string
                else:
                    arithmetic_returned = return_string
                return_string = str(arithmetic_returned)
            elif op in bool_bool:
                #HERE
                if left_bool is not None and right_bool is not None:
                    if op == "&":
                        boolean_returned = left_bool and right_bool
                    elif op == "|":
                        boolean_returned = left_bool or right_bool
                    else:
                        boolean_returned = return_string
                else: 
                    boolean_returned = return_string
                return_string = str(boolean_returned)
            
            if remaining_string != None:
                return_string = return_string + remaining_string

            return return_string
    
    # Visit a parse tree produced by LambdaCalculusParser#value.
    def visitValue(self, ctx:LambdaCalculusParser.ValueContext):
        parenthesis_check = ctx.getChild(0).getText()
        if parenthesis_check == "(":
            return ctx.getChild(1).getText()
        else:
            return ctx.getText()


    # Visit a parse tree produced by LambdaCalculusParser#variable.
    def visitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        return ctx.getText()


    # Visit a parse tree produced by LambdaCalculusParser#number.
    def visitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        return ctx.getText()


    # Visit a parse tree produced by LambdaCalculusParser#boolean_value.
    def visitBoolean_value(self, ctx:LambdaCalculusParser.Boolean_valueContext):
        return ctx.getText()


    # Visit a parse tree produced by LambdaCalculusParser#operation.
    def visitOperation(self, ctx:LambdaCalculusParser.OperationContext):
        return ctx.getText()

    
