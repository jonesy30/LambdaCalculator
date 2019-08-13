# Generated from arithmetic.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .arithmeticParser import arithmeticParser
else:
    from arithmeticParser import arithmeticParser

# This class defines a complete listener for a parse tree produced by arithmeticParser.
class arithmeticListener(ParseTreeListener):

    # Enter a parse tree produced by arithmeticParser#function.
    def enterFunction(self, ctx:arithmeticParser.FunctionContext):
        pass

    # Exit a parse tree produced by arithmeticParser#function.
    def exitFunction(self, ctx:arithmeticParser.FunctionContext):
        pass


    # Enter a parse tree produced by arithmeticParser#multiplyingExpression.
    def enterMultiplyingExpression(self, ctx:arithmeticParser.MultiplyingExpressionContext):
        pass

    # Exit a parse tree produced by arithmeticParser#multiplyingExpression.
    def exitMultiplyingExpression(self, ctx:arithmeticParser.MultiplyingExpressionContext):
        pass


    # Enter a parse tree produced by arithmeticParser#atom.
    def enterAtom(self, ctx:arithmeticParser.AtomContext):
        pass

    # Exit a parse tree produced by arithmeticParser#atom.
    def exitAtom(self, ctx:arithmeticParser.AtomContext):
        pass


    # Enter a parse tree produced by arithmeticParser#variable.
    def enterVariable(self, ctx:arithmeticParser.VariableContext):
        pass

    # Exit a parse tree produced by arithmeticParser#variable.
    def exitVariable(self, ctx:arithmeticParser.VariableContext):
        pass


    # Enter a parse tree produced by arithmeticParser#number.
    def enterNumber(self, ctx:arithmeticParser.NumberContext):
        pass

    # Exit a parse tree produced by arithmeticParser#number.
    def exitNumber(self, ctx:arithmeticParser.NumberContext):
        pass


    # Enter a parse tree produced by arithmeticParser#boolean_value.
    def enterBoolean_value(self, ctx:arithmeticParser.Boolean_valueContext):
        pass

    # Exit a parse tree produced by arithmeticParser#boolean_value.
    def exitBoolean_value(self, ctx:arithmeticParser.Boolean_valueContext):
        pass


