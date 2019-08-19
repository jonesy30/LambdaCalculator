from LambdaCalculusVisitor import LambdaCalculusVisitor
from AlphaCalculatorPartial import calculate_alpha
from Stack import Stack
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
else:
    from LambdaCalculusParser import LambdaCalculusParser
from BaseVisitor import BaseVisitor
from BetaReductionFileWriter import BetaReductionFileWriter
import re

class CallByNameVisitor(BaseVisitor):

    def __init__(self):
        super()
        self.incoming_values = Stack() #NOTE: This definitely needs renamed
        self.valid_typing = True

        self.super_typing_context = []
        self.current_typing_context = []

        self.beta_reduction_writer = BetaReductionFileWriter()

        self.beta_reduction_writer.write_to_file("Call by name visitor selected")
    
    # Visit a parse tree produced by LambdaCalculusParser#application.
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        
        #print("Application = "+ctx.getText())

        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        #Visit the first child, then visit the second
        self.beta_reduction_writer.write_to_file("In application "+ctx.getText()+", node "+ctx.getChild(0).getText()+" being processed")
        returned_child = self.visit(ctx.getChild(0))
        function = returned_child[0]
        function_type = returned_child[1]

        input_type = None
        if len(returned_child) == 3:
            input_type = returned_child[2]
            
        self.beta_reduction_writer.write_to_file("In application "+ctx.getText()+", node "+ctx.getChild(1).getText()+" being passed to "+str(function))
        expression = ctx.getChild(1).getText()
        expression_type = None

        #Get the tree created by the output of the left hand tree
        tree = self.create_tree(function)

        #Find the type of the first root node (ignoring terms)
        am_I_an_abstraction = tree
        while isinstance(am_I_an_abstraction,LambdaCalculusParser.TermContext):
            am_I_an_abstraction = am_I_an_abstraction.getChild(0)

        application_type = None

        #If the left hand tree is an abstraction - you're not done! Keep processing using the right hand side of the tree
        if isinstance(am_I_an_abstraction,LambdaCalculusParser.AbstractionContext):
            #Visit the left hand tree with the term created from the right hand side
            self.incoming_values.push(expression)
            function,function_type = self.visit(am_I_an_abstraction)
            application_type = function_type

        #The left hand side isn't an abstraction, keep the left hand side as it is, and add the right
        else:
            expression, expression_type = self.visit(ctx.getChild(1))
            function = str(function) + str(expression)
            #Get the type of the application based on the two incoming values
            application_type = self.type_check_application(function_type,expression_type)

        #Return the application value and type
        #print("Returned value in application = "+function)
        return function,application_type

    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        #print("Abstraction = "+ctx.getText())

        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        #At each abstraction, if the bound variable is repeated then change all other instances of this in the list to avoid conflicts
        bound_variable = ctx.getChild(0).getChild(1).getChild(0).getText()

        self.update_typing_contexts(bound_variable)

        #NOTE: These all definitely need renamed
        #Visit the left hand child, to get the bound variable type and value
        to_substitute,to_substitute_type = self.visit(ctx.getChild(0))

        #Pop the value as soon as you get the abstraction term, before you
        #visit the rest of the children, so the correct term gets associated
        #with the correct input
        incoming = self.incoming_values.pop()
        incoming_type = None

        abstraction_result, abstraction_type = self.perform_abstraction(ctx, incoming, incoming_type, to_substitute, to_substitute_type)
        if incoming != -1:
            abstraction_type = self.type_check_application(abstraction_type,incoming_type)

        return abstraction_result,abstraction_type