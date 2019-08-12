
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

class AlphaConversionVisitor(LambdaCalculusVisitor):

    def __init__(self):
        super()
        self.incoming_values = Stack() #NOTE: This definitely needs renamed
        self.alpha_calculator = AlphaCalculatorFromComplete()

    # Visit a parse tree produced by LambdaCalculusParser#term.
    def visitTerm(self, ctx:LambdaCalculusParser.TermContext):
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        print("In term "+ctx.getText())
        return self.visitChildren(ctx)

    # Application needs to change to:
    # visit(0), visit(1), return the string of them both
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        print("In applicaiton "+ctx.getText())

        #Check for parentheses
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        right_child = self.visit(ctx.getChild(1))
        print("Right child = "+str(right_child))
        if right_child != None:
            self.incoming_values.push(right_child)
        
        left_child = self.visit(ctx.getChild(0))

        returned_result = "" + left_child + right_child

        return returned_result

    # Abstraction needs to become an alpha-converter (after having visited children)
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        print("In abstraction "+ctx.getText())
        #Check for parentheses
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        #inner_expression = self.visit(ctx.getChild(2))
        inner_expression = ctx.getChild(2).getText()
        complete_expression = "" + ctx.getChild(0).getText() + ctx.getChild(1).getText() + inner_expression
        print("Complete expression = "+str(complete_expression))

        incoming = self.incoming_values.pop()
        print("In abstraction, incoming = "+str(incoming))

        if incoming != -1:
            returned_abstraction = self.alpha_calculator.calculate_alpha(complete_expression, incoming)
        else:
            returned_abstraction = self.alpha_calculator.calculate_alpha(complete_expression, None)

        return returned_abstraction

    def visitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        return ctx.getText()

    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):
        #Check for parentheses
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        #We're not doing any evaluation here, we just want the textual representation of the function
        return self.visit(ctx.getChild(0)) + ctx.getChild(1).getText() + self.visit(ctx.getChild(2))

    def visitValue(self, ctx:LambdaCalculusParser.ValueContext):
        #Check for parentheses
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        return self.visitChildren(ctx)

    def visitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        #We don't care about types for alpha conversion, so just return the value of the variable and ignore the type
        return ctx.getChild(0).getText()

    def visitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        return ctx.getChild(0).getText()

    def visitBoolean_value(self, ctx:LambdaCalculusParser.Boolean_valueContext):
        return ctx.getChild(0).getText()

    def check_for_parenthesis(self, ctx):
        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()
        else:
            return -1