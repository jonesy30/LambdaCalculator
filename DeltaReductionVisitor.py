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

#Class which implements delta reduction (arithmetic evaluation) using an ANTLR visitor which navigates around an abstract syntax tree

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
            #We don't care about processing applications in this visitor, just about evaluating functions, so visit the
            #left and right child and return the result of them both
            return self.visit(ctx.getChild(0)) + self.visit(ctx.getChild(1))

    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()
        else:
            #Get the result of the right child (M in %x.M) and keep it around
            #since in arithmetic evaluation we don't care about processing abstractions, just evaluating functions
            right_child = self.visit(ctx.getChild(2))
            return ctx.getChild(0).getText() + ctx.getChild(1).getText() + right_child

    # Visit a parse tree produced by LambdaCalculusParser#abstraction_term.
    def visitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        #The abstraction terms (in form %x. ) just return the text as is
        return ctx.getText()

    # Visit a parse tree produced by LambdaCalculusParser#function.
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):

        #Operations which take a boolean for their left and right hand children
        bool_bool = ["&","|"]
        #Operations which take an integer for their left and right hand children
        int_int = ["+","-","*","/","^","==",">","<"]

        parenthesis_check = ctx.getChild(0).getText()
        #If I am a function contained in parenthesis, work out if I can remove the parenthesis or not
        if parenthesis_check == "(":
            inner_function = self.visit(ctx.getChild(1))

            #If the function inside the parenthesis is still a function, leave the brackets as is 
            for operation in bool_bool:
                if operation in inner_function:
                    return "" + ctx.getChild(0).getText() + inner_function + ctx.getChild(2).getText()
            for operation in int_int:
                if operation in inner_function:
                    return "" + ctx.getChild(0).getText() + inner_function + ctx.getChild(2).getText()
            #If the function reaches this point the inner term is not a function, so safe to remove parentheses, for example (3) is the same as 3
            return inner_function
        else:
            #If I am not a function contained in parenthesis, visit the left and right child to get the result of both
            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))

            #A regex to match a positive number 0-99999999...
            number_regex = "^0|^[1-9][0-9]*$"

            left_number = None
            right_number = None

            #Find whether or not the left and right terms are numbers, and store if so
            if re.match(number_regex, left):
                left_number = left    
            if re.match(number_regex, right):
                right_number = right

            left_bool = None
            right_bool = None

            #Find whether or not the left and right terms are boolean values, and store if so
            if left == 'TRUE' or left == 'true' or left == 'True':
                left_bool = True
            elif left == 'FALSE' or left == 'false' or left == 'False':
                left_bool = False
            if right == 'TRUE' or right == 'true' or right == 'True':
                right_bool = True
            elif right == 'FALSE' or right == 'false' or right == 'False':
                right_bool = False

            #Get the operation which is to be used to calculate the result
            op = ctx.getChild(1).getText()
            
            #If the right-term is not a boolean or an int (for example 2+%x.x+1 which is an abstraction)
            #extract the the left-hand part of the right-hand term
            #remaining_string is what's left after a number or boolean has been extracted
            remaining_string = None
            if right_number == None and right_bool == None:
                #If the first part of the right-hand side is a number, save it and the remaining part of the term
                right_left_match = re.search("^0|^[1-9][0-9]*", right)
                if right_left_match!=None and left_number!=None:
                    right_number = right_left_match.group(0)
                    remaining_string = re.sub("^0|^[1-9][0-9]*", "", right, 1)

                #If the first part of the right-hand side is a boolean, save it and the remaining part of the term
                right_left_match = re.search("^[Tt][Rr][Uu][Ee]|^[Ff][Aa][Ll][Ss][Ee]", right)
                if right_left_match!=None and left_bool!=None:
                    right_bool = right_left_match.group(0)
                    remaining_string = re.sub("^[Tt][Rr][Uu][Ee]|^[Ff][Aa][Ll][Ss][Ee]", "", right, 1)

            #Just incase the function can't be evaluated, save the original unprocessed function which is then overridden
            return_string = "" + left + op + right
            #If the operation takes an integer for the left and right hand nodes
            if op in int_int:
                #If both the left and right and term are both integers, perform the calculation
                if left_number is not None and right_number is not None:
                    if op == "+":
                        arithmetic_returned = int(left_number) + int(right_number)
                    elif op == "-":
                        arithmetic_returned = int(left_number) - int(right_number)
                    elif op == "*":
                        arithmetic_returned = int(left_number) * int(right_number)
                    elif op == "/":
                        #Floor divide if division to avoid decimal points
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
                        #If the operation isn't recognised (for some reason), keep the return string as is
                        arithmetic_returned = return_string
                else:
                    #if either the left or right isn't a number, just keep the term as it is
                    arithmetic_returned = return_string
                #Get the string version of the arithmetic value returned
                return_string = str(arithmetic_returned)
            elif op in bool_bool:
                #Perform boolean operations if the operation is a boolean operation
                if left_bool is not None and right_bool is not None:
                #If both sides are boolean values, perform the boolean operations
                    if op == "&":
                        boolean_returned = left_bool and right_bool
                    elif op == "|":
                        boolean_returned = left_bool or right_bool
                    else:
                        boolean_returned = return_string
                else:
                    #if either the left or right isn't a boolean, just keep the term as it is
                    boolean_returned = return_string
                return_string = str(boolean_returned)
            
            #If there is any part of the term which hasn't been dealt with (for example if it is in abstraction form), add it to the resultant string
            if remaining_string != None:
                return_string = return_string + remaining_string

            #Return the final arithmetically evaluated term
            return return_string
    
    # Visit a parse tree produced by LambdaCalculusParser#value.
    def visitValue(self, ctx:LambdaCalculusParser.ValueContext):
        #A value is either a number, a boolean or a variable
        #Check for parentheses and return the middle section if it is (without the brackets since they are not needed with single values)
        parenthesis_check = ctx.getChild(0).getText()
        if parenthesis_check == "(":
            return ctx.getChild(1).getText()
        else:
            return ctx.getText()


    # Visit a parse tree produced by LambdaCalculusParser#variable.
    def visitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        #If the term is a variable (letter), just return the textual representation of that value
        return ctx.getText()


    # Visit a parse tree produced by LambdaCalculusParser#number.
    def visitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        #If the term is a number, just return the textual representation of that number
        return ctx.getText()


    # Visit a parse tree produced by LambdaCalculusParser#boolean_value.
    def visitBoolean_value(self, ctx:LambdaCalculusParser.Boolean_valueContext):
        #If the term is a boolean, just return the textual representation of that boolean
        return ctx.getText()


    # Visit a parse tree produced by LambdaCalculusParser#operation.
    def visitOperation(self, ctx:LambdaCalculusParser.OperationContext):
        #If the term is an operation, just return the textual representation of that operation
        return ctx.getText()

    
