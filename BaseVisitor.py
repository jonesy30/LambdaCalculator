from LambdaCalculusVisitor import LambdaCalculusVisitor
from AlphaCalculatorPartial import calculate_alpha
from Stack import Stack
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
    from .LambdaCalculusLexer import LambdaCalculusLexer
else:
    from LambdaCalculusParser import LambdaCalculusParser
    from LambdaCalculusLexer import LambdaCalculusLexer
import re

class BaseVisitor(LambdaCalculusVisitor):

    def __init__(self):
        super()
    
    # Visit a parse tree produced by LambdaCalculusParser#term.
    def visitTerm(self, ctx:LambdaCalculusParser.TermContext):
        print("T: "+ctx.getText())

        depth = ctx.depth()
        if depth == 1:
            
            output,return_type = self.visitChildren(ctx)

            output,return_type = self.post_process(output, return_type)
            return output,return_type,self.valid_typing

        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#function.
    #NOTE: having function_type = None could be a way to fix my "invalid typing when bound variable does not match inner variable" issue
    #Just call this method directly from the abstraction term if the thing below is a function
    #NOTE: If I don't end up needing this, take it out!
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext, function_type=None):
        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            child_value,child_type = self.visit(ctx.getChild(1))
            return "" + ctx.getChild(0).getText() + child_value + ctx.getChild(2).getText(),child_type
        
        #NOTE: I should be calculating the function here and returning the result
        left,left_type = self.visit(ctx.getChild(0))
        #TODO: Determine the typing rules here
        right,right_type = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()

        if left_type is not None:
            left_type = left_type.lower()
        
        if right_type is not None:
            right_type = right_type.lower()

        #Functions that take two booleans and return a boolean
        bool_bool = ["AND","OR"]
        #Take two ints and return an int
        int_int = ["+","-","*","/","^"]
        #Takes two ints and returns a boolean
        int_bool = ["EQ","GT","LT"]
        return_type = None

        if op in bool_bool:
            if left_type == "int" or right_type == "int":
                self.valid_typing = False
            elif self.valid_typing == True:
                return_type = "bool"
        elif op in int_int or op in int_bool:
            if left_type == "bool" or right_type == "bool":
                self.valid_typing = False
            elif self.valid_typing == True:
                return_type = "int"
        
        #TODO: Do some actual calculations here
        return_string = "" + left + op + right
        
        return return_string,return_type
    
    # Visit a parse tree produced by LambdaCalculusParser#variable.
    def visitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        if ctx.getChild(2) is None:
            return ctx.getChild(0).getText(),None
        else:
            return ctx.getChild(0).getText(),self.visit(ctx.getChild(2))

    # Visit a parse tree produced by LambdaCalculusParser#abstraction_term.
    def visitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        return self.visit(ctx.getChild(1))
        #return self.visitChildren(ctx)
        
    # Visit a parse tree produced by LambdaCalculusParser#number.
    def visitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        if ctx.getChild(2) is None:
            return ctx.getChild(0).getText(),None
        else:
            return ctx.getChild(0).getText(),self.visit(ctx.getChild(2))

        #return ctx.getChild(0).getText()
        #return self.visitChildren(ctx)
    
    # Visit a parse tree produced by LambdaCalculusParser#operation.
    def visitOperation(self, ctx:LambdaCalculusParser.OperationContext):
        return self.visitChildren(ctx)
    
    
    # Visit a parse tree produced by LambdaCalculusParser#expression.
    def visitValue(self, ctx:LambdaCalculusParser.ValueContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by LambdaCalculusParser#term_type.
    def visitFunction_type(self, ctx:LambdaCalculusParser.Function_typeContext):
        return ctx.getText()

    #NOTE: Please rename this future Yola...
    def convert_function_with_type(self, to_substitute, to_substitute_type, incoming, incoming_type, function, end_value=None):

        #If there is a bound variable type to be substituted, add it to the rest of the bound variables in the term
        if to_substitute_type is not None:
            print(str(to_substitute_type))
            #incoming = incoming + ":" + incoming_type
            incoming = incoming + ":" + to_substitute_type

            function = function[:end_value].replace(to_substitute,incoming) + function[end_value:]
        
        #If the substituted type is none but the incoming type is not, we still know what the bound variable type should now be, so replace it
        elif incoming_type is not None:
            print("To substitute type is none, but incoming isn't!")
            incoming = incoming + ":" + incoming_type
            function = function[:end_value].replace(to_substitute,incoming) + function[end_value:]

        return function

    def type_check_application(self, function_type, expression_type):
        #Type check the application
        application_type_journey = []

        if function_type is not None:
            #Split the type of the function term into their journeys (1 -> 2 -> 3 -> ...n)
            print("Function type not none! "+function_type)
            function_type_journey = function_type.split("->")
            if expression_type is not None:
                #Do the same splitting with the type of the expression
                print("Expression type = "+expression_type)
                expression_type_journey = expression_type.split("->")
                application_type_journey = []

                #Check whether the typing is valid or not
                if len(function_type_journey) > len(expression_type_journey):
                    type_mismatch = False
                    while len(expression_type_journey) > 0:
                        if function_type_journey[0] != expression_type_journey[0]:
                            function_journey_step = function_type_journey[0].lower()
                            expression_journey_step = expression_type_journey[0].lower()
                            if function_journey_step == "none" or expression_journey_step == "none":
                                expression_type_journey = []
                                type_mismatch = True
                            else:
                                #NOTE: Repeated code
                                del function_type_journey[0]
                                del expression_type_journey[0]
                        else:
                            del function_type_journey[0]
                            del expression_type_journey[0]
                    if type_mismatch == False:
                        application_type_journey = function_type_journey
            else:
                print("Function type journey = "+str(function_type_journey))
                del function_type_journey[0]
                application_type_journey = function_type_journey
    
        if application_type_journey == [] or application_type_journey == None:
            application_type = "None"
        else:
            #Create the abstraction type string based on what's left of the function type term
            print("Application_type_journey = "+str(application_type_journey))
            application_type = ""
            for i,journey_step in enumerate(application_type_journey):
                application_type = application_type + "->" + application_type_journey[i]
            application_type=application_type[2:]
    
        return application_type

    def convert_type_if_none(self, term_type):
        
        if term_type is not None:
            term_type = term_type.lower()
            if term_type == "none":
                term_type = None
            
        return term_type

    def post_process(self, output, return_type):

        bad_strings = [":int",":Int",":INT",":bool",":Bool",":BOOL",":None",":NONE",":none"]

        output = str(output)
        return_type = str(return_type)
        for string in bad_strings:
            output = output.replace(string,"")

        return output,return_type

    def create_tree(self, function):
        stream = InputStream(function)
        lexer = LambdaCalculusLexer(stream)
        tokens = CommonTokenStream(lexer)
        parser = LambdaCalculusParser(tokens)
        tree = parser.term()

        return tree