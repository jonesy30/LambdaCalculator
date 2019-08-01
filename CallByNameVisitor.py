from LambdaCalculusVisitor import LambdaCalculusVisitor
from AlphaCalculatorPartial import calculate_alpha
from Stack import Stack
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
else:
    from LambdaCalculusParser import LambdaCalculusParser
from BaseVisitor import BaseVisitor
import re

class CallByNameVisitor(BaseVisitor):

    def __init__(self):
        super()
        self.incoming_values = Stack() #NOTE: This definitely needs renamed
        self.valid_typing = True
    
    # Visit a parse tree produced by LambdaCalculusParser#application.
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        
        print("Application = "+ctx.getText())

        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

        #Visit the first child, then visit the second
        #NOTE: To convert to call-by-name, I need to get the text of child 1, and then evaluate the abstraction with the unprocessed textual version of child 1
        #Then I need to get the abstraction to create a tree of the result of itself (before or after alpha conversion?) which it will then visit and process
        function,function_type = self.visit(ctx.getChild(0))
        expression = ctx.getChild(1).getText()
        expression_type = None
        #expression,expression_type = self.visit(ctx.getChild(1))

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
            function = function + expression
            #Get the type of the application based on the two incoming values
            application_type = self.type_check_application(function_type,expression_type)

        print("Application_type = "+str(application_type))

        #Return the application value and type
        print("Returned value in application = "+function)
        return function,application_type

    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        print("Abstraction = "+ctx.getText())

        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check

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

        print("Abstraction type = "+abstraction_type)
        return abstraction_result,abstraction_type