
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

#Class which is called when the user selects "alpha-conversion only" from the web interface
#Converts a lambda term and outputs the result using alpha-conversion alone (no beta-reduction)
#This produces a term which is in the same form but which would not cause variable conflicts if it was passed through a function
#(the beta-reduction evaluations do this implicitly)

class AlphaConversionVisitor(LambdaCalculusVisitor):

    def __init__(self):
        super()

        #incoming_values are the values which are being passed from applications to abstractions for substitution
        self.incoming_values = Stack()
        self.alpha_calculator = AlphaCalculatorFromComplete()

    #Visit a term node - just check for parentheses and return as I am
    def visitTerm(self, ctx:LambdaCalculusParser.TermContext):
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        return self.visitChildren(ctx)

    #Visit an application node - push the right-hand-node to the left-hand-node for processing by abstractions
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        #Check for parentheses
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        #Get the right child and pass it to the left if one exists
        right_child = self.visit(ctx.getChild(1))
        if right_child != None:
            self.incoming_values.push(right_child)
        
        #Get the left child
        left_child = self.visit(ctx.getChild(0))

        #The resultant application is the processed left child + the processed right child
        returned_result = "" + left_child + right_child

        return returned_result

    #Visit an abstraction - get the incoming term from the application stack and alpha-convert the term
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        #Check for parentheses
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        #Get the inner term (the x+1 part of %x.x+1)
        inner_expression = ctx.getChild(2).getText()
        #Get the complete expression
        complete_expression = "" + ctx.getChild(0).getText() + ctx.getChild(1).getText() + inner_expression

        incoming = self.incoming_values.pop()

        #Alpha convert the complete expression with the incoming variable
        if incoming != -1:
            returned_abstraction = self.alpha_calculator.calculate_alpha(complete_expression, incoming)
        else:
            returned_abstraction = self.alpha_calculator.calculate_alpha(complete_expression, None)

        return returned_abstraction

    #Visit an abstraction_term - just return the textual representation of what I am without any processing
    def visitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        return ctx.getText()

    #Visit a function - just return the textual representation of what I am without processing (since I'm not doing any beta-reduction)
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):
        #Check for parentheses
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        #We're not doing any evaluation here, we just want the textual representation of the function
        return self.visit(ctx.getChild(0)) + ctx.getChild(1).getText() + self.visit(ctx.getChild(2))

    #Visit a value - return the result of my children
    def visitValue(self, ctx:LambdaCalculusParser.ValueContext):
        #Check for parentheses
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        return self.visitChildren(ctx)

    #Visit a Variable - just return the text of my left child (since types could be the right child and types are ignored in alpha-conversion)    
    def visitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        #We don't care about types for alpha conversion, so just return the value of the variable and ignore the type
        return ctx.getChild(0).getText()

    #Visit a Number - just return the text of my left child (since types could be the right child and types are ignored in alpha-conversion) 
    def visitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        return ctx.getChild(0).getText()

    #Visit a Boolean_value - just return the text of my left child (since types could be the right child and types are ignored in alpha-conversion) 
    def visitBoolean_value(self, ctx:LambdaCalculusParser.Boolean_valueContext):
        return ctx.getChild(0).getText()

    #Function which checks for parenthesis and returns the visited inner term while keeping the brackets around
    def check_for_parenthesis(self, ctx):
        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()
        else:
            return -1