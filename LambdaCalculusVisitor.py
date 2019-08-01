# Generated from LambdaCalculus.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
else:
    from LambdaCalculusParser import LambdaCalculusParser

# This class defines a complete generic visitor for a parse tree produced by LambdaCalculusParser.

class LambdaCalculusVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LambdaCalculusParser#term.
    def visitTerm(self, ctx:LambdaCalculusParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaCalculusParser#application.
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaCalculusParser#abstraction_term.
    def visitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaCalculusParser#function.
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaCalculusParser#value.
    def visitValue(self, ctx:LambdaCalculusParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaCalculusParser#variable.
    def visitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaCalculusParser#number.
    def visitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaCalculusParser#boolean_value.
    def visitBoolean_value(self, ctx:LambdaCalculusParser.Boolean_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaCalculusParser#function_type.
    def visitFunction_type(self, ctx:LambdaCalculusParser.Function_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaCalculusParser#ground_type.
    def visitGround_type(self, ctx:LambdaCalculusParser.Ground_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaCalculusParser#operation.
    def visitOperation(self, ctx:LambdaCalculusParser.OperationContext):
        return self.visitChildren(ctx)



del LambdaCalculusParser