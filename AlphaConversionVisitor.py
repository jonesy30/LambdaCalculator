
from LambdaCalculusVisitor import LambdaCalculusVisitor
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
    from .LambdaCalculusLexer import LambdaCalculusLexer
else:
    from LambdaCalculusParser import LambdaCalculusParser
    from LambdaCalculusLexer import LambdaCalculusLexer
import re

class AlphaConversionVisitor(LambdaCalculusVisitor):

    # Application needs to change to:
    # visit(0), visit(1), return the string of them both
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        #Check for parentheses
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        return self.visitChildren(ctx)

    # Abstraction needs to become an alpha-converter (after having visited children)
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        #Check for parentheses
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        return self.visitChildren(ctx)

    def visitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        #We are only interested in the variable associated with this term, not the % part
        return self.visit(ctx.getChild(1))

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