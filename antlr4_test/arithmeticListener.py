# Generated from arithmetic.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .arithmeticParser import arithmeticParser
else:
    from arithmeticParser import arithmeticParser

# This class defines a complete listener for a parse tree produced by arithmeticParser.
class arithmeticListener(ParseTreeListener):

    # Enter a parse tree produced by arithmeticParser#foo.
    def enterFoo(self, ctx:arithmeticParser.FooContext):
        pass

    # Exit a parse tree produced by arithmeticParser#foo.
    def exitFoo(self, ctx:arithmeticParser.FooContext):
        pass


    # Enter a parse tree produced by arithmeticParser#equation.
    def enterEquation(self, ctx:arithmeticParser.EquationContext):
        pass

    # Exit a parse tree produced by arithmeticParser#equation.
    def exitEquation(self, ctx:arithmeticParser.EquationContext):
        pass


    # Enter a parse tree produced by arithmeticParser#expression.
    def enterExpression(self, ctx:arithmeticParser.ExpressionContext):
        pass

    # Exit a parse tree produced by arithmeticParser#expression.
    def exitExpression(self, ctx:arithmeticParser.ExpressionContext):
        pass


    # Enter a parse tree produced by arithmeticParser#variable.
    def enterVariable(self, ctx:arithmeticParser.VariableContext):
        pass

    # Exit a parse tree produced by arithmeticParser#variable.
    def exitVariable(self, ctx:arithmeticParser.VariableContext):
        pass


