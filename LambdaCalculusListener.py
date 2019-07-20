# Generated from LambdaCalculus.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
else:
    from LambdaCalculusParser import LambdaCalculusParser

# This class defines a complete listener for a parse tree produced by LambdaCalculusParser.
class LambdaCalculusListener(ParseTreeListener):

    # Enter a parse tree produced by LambdaCalculusParser#term.
    def enterTerm(self, ctx:LambdaCalculusParser.TermContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#term.
    def exitTerm(self, ctx:LambdaCalculusParser.TermContext):
        pass


    # Enter a parse tree produced by LambdaCalculusParser#value.
    def enterValue(self, ctx:LambdaCalculusParser.ValueContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#value.
    def exitValue(self, ctx:LambdaCalculusParser.ValueContext):
        pass


    # Enter a parse tree produced by LambdaCalculusParser#function.
    def enterFunction(self, ctx:LambdaCalculusParser.FunctionContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#function.
    def exitFunction(self, ctx:LambdaCalculusParser.FunctionContext):
        pass


    # Enter a parse tree produced by LambdaCalculusParser#abstraction.
    def enterAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#abstraction.
    def exitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        pass


    # Enter a parse tree produced by LambdaCalculusParser#abstraction_term.
    def enterAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#abstraction_term.
    def exitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        pass


    # Enter a parse tree produced by LambdaCalculusParser#application.
    def enterApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#application.
    def exitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        pass


    # Enter a parse tree produced by LambdaCalculusParser#variable.
    def enterVariable(self, ctx:LambdaCalculusParser.VariableContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#variable.
    def exitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        pass


    # Enter a parse tree produced by LambdaCalculusParser#lambda_variable.
    def enterLambda_variable(self, ctx:LambdaCalculusParser.Lambda_variableContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#lambda_variable.
    def exitLambda_variable(self, ctx:LambdaCalculusParser.Lambda_variableContext):
        pass


    # Enter a parse tree produced by LambdaCalculusParser#number.
    def enterNumber(self, ctx:LambdaCalculusParser.NumberContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#number.
    def exitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        pass


    # Enter a parse tree produced by LambdaCalculusParser#operation.
    def enterOperation(self, ctx:LambdaCalculusParser.OperationContext):
        pass

    # Exit a parse tree produced by LambdaCalculusParser#operation.
    def exitOperation(self, ctx:LambdaCalculusParser.OperationContext):
        pass


