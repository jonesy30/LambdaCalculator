from LambdaCalculusVisitor import LambdaCalculusVisitor
from AlphaCalculatorPartial import calculate_alpha
from Stack import Stack
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
else:
    from LambdaCalculusParser import LambdaCalculusParser
from BaseVisitor import BaseVisitor
from LambdaSessionInformationObject import LambdaSessionInformationObject
import re

#Class which implements call-by-name beta evaluation using an ANTLR visitor which navigates around an abstract syntax tree

class CallByNameVisitor(BaseVisitor):

    def __init__(self,session_object):
        super()
        self.incoming_values = Stack()
        self.valid_typing = True

        #Typing context is used to differentiate between the current scope typing and the main scope typing
        self.super_typing_context = []
        self.current_typing_context = []

        #Session object is used to pass information between webpages
        self.session_object = session_object

        self.session_object.add_beta_step("Call by name visitor selected")
    
    # Visit a parse tree produced by LambdaCalculusParser#application.
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        
        #Check for parenthesis, and return the inner bit if so
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        #Visit the first child, then visit the second
        self.session_object.add_beta_step("In application "+ctx.getText()+", node "+ctx.getChild(0).getText()+" being evaluated using the left-reduction rule")
        returned_child = self.visit(ctx.getChild(0))
        
        #Get the function and function type from the returned child
        function = returned_child[0]
        function_type = returned_child[1]

        #If there are still variables to unpack, it's the typing inference of the input term from a  function. Unpack this
        input_type = None
        if len(returned_child) == 3:
            input_type = returned_child[2]
            
        self.session_object.add_beta_step("In application "+ctx.getText()+", node "+ctx.getChild(1).getText()+" being passed to "+str(function))
        #Get the text of the left hand term
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
        return function,application_type

    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):

        #Check whether the abstraction is contained in parentheses, and return if so
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        #At each abstraction, if the bound variable is repeated then change all other instances of this in the list to avoid conflicts
        bound_variable = ctx.getChild(0).getChild(1).getChild(0).getText()

        #Update the typing context with this bound variable
        self.update_typing_contexts(bound_variable)

        #Visit the left hand child, to get the bound variable type and value
        to_substitute,to_substitute_type = self.visit(ctx.getChild(0))

        #Pop the value as soon as you get the abstraction term, before you
        #visit the rest of the children, so the correct term gets associated
        #with the correct input
        incoming = self.incoming_values.pop()
        incoming_type = None

        #Perform the bulk of the abstraction (contained within BaseVisitor) and get the result and type of the abstraction
        abstraction_result, abstraction_type = self.perform_abstraction(ctx, incoming, incoming_type, to_substitute, to_substitute_type)
        
        #If there is an incoming value, type check the application now processing is complete
        if incoming != -1:
            abstraction_type = self.type_check_application(abstraction_type,incoming_type)

        #Return the results of the abstraction
        return abstraction_result,abstraction_type