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

class MyLambdaVisitor(LambdaCalculusVisitor):

    #NOTE: Sort out the order of these functions so it makes more sense!
    def __init__(self):
        super()
        self.incoming_values = Stack() #NOTE: This definitely needs renamed

    # Visit a parse tree produced by LambdaCalculusParser#application.
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        
        print("Application = "+ctx.getText())

        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            child_value,child_type = self.visit(ctx.getChild(1))
            return "" + ctx.getChild(0).getText() + child_value + ctx.getChild(2).getText(),child_type

        function,function_type = self.visit(ctx.getChild(0))
        expression,expression_type = self.visit(ctx.getChild(1))

        #NOTE: I definitely don't need to change form any more
        function = self.convert_back_abstraction_form(function)
        expression = self.convert_back_abstraction_form(expression)

        #Get the tree created by the output of the left hand tree
        stream = InputStream(function)
        lexer = LambdaCalculusLexer(stream)
        tokens = CommonTokenStream(lexer)
        parser = LambdaCalculusParser(tokens)
        tree = parser.term()

        #Find the type of the first root node (ignoring terms)
        am_I_an_abstraction = tree
        while isinstance(am_I_an_abstraction,LambdaCalculusParser.TermContext):
            #print("Term in tree = "+str(type(am_I_an_abstraction)))
            am_I_an_abstraction = am_I_an_abstraction.getChild(0)

        #print("Term in tree = "+str(type(am_I_an_abstraction)))
        #If the left hand tree is an abstraction - you're not done! Keep processing using the right hand side of the tree
        if isinstance(am_I_an_abstraction,LambdaCalculusParser.AbstractionContext):
            self.incoming_values.push(tuple([expression,expression_type]))
            function,function_type = self.visit(am_I_an_abstraction)
        else:
            function = function + expression

        print("Returned value in application = "+function)
        return function,function_type
    
    # Visit a parse tree produced by LambdaCalculusParser#term.
    def visitTerm(self, ctx:LambdaCalculusParser.TermContext):
        print("T: "+ctx.getText())

        #NOTE: do I need a parenthesis check in here? I don't think I do, since I'm just returning children
        #The abstraction puts lambda terms into [?/x] form, this chunk of code just converts it back before it gets
        #passed to the user for readability
        depth = ctx.depth()
        if depth == 1:
            
            #output,return_type = str(self.visitChildren(ctx))
            output,return_type = self.visitChildren(ctx)
            output = str(output)
            return_type = str(return_type)
            #returned = str(self.visitChildren(ctx))
            #NOTE: do I need this in here if I'm just doing the same thing in the abstraction? Or should I just get rid of this
            #NOTE: string manipulation altogether?
            output = self.convert_back_abstraction_form(output)            
            return output,return_type

        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        print("Abstraction = "+ctx.getText())

        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            child_value,child_type = self.visit(ctx.getChild(1))
            return "" + ctx.getChild(0).getText() + child_value + ctx.getChild(2).getText(),child_type
        
        #Pop the value as soon as you get the abstraction term, before you
        #visit the rest of the children, so the correct term gets associated
        #with the correct input
        
        #NOTE: These all definitely need renamed
        to_substitute,to_substitute_type = self.visit(ctx.getChild(0))
        incoming = self.incoming_values.pop()
        incoming_type = None
        if isinstance(incoming,tuple):
            incoming = incoming[0]
            incoming_type = incoming[1]
        print("Popped type = "+str(incoming_type))
        function,function_type = self.visit(ctx.getChild(2))

        print("To substitute = "+to_substitute)
        print("Function before abstraction = "+function)
        print("Incoming before abstraction = "+str(incoming))

        new_function = function
        if incoming != -1:
            bound_variables_left = re.findall("/(.*?)\]", function)
            subst_container_match = re.search("\[(.*?)\]", function)
            
            if subst_container_match is not None:
                container = subst_container_match.group(0)

                end_value = len(function)
                if len(bound_variables_left) > 0:
                    #More than one bound variable -- do something here
                    if to_substitute in bound_variables_left:
                        #Bound variable repeated, need to check for the next instance of it
                        for i,letter in enumerate(function):
                            if letter == '[':
                                subst_container_match = re.search("/(.*?)\]", function[i:])
                                bound_value = subst_container_match.group(1)
                                if to_substitute == bound_value:
                                    break
                        end_value = i
                        function = calculate_alpha(to_substitute, function, incoming, 0, end_value)
                    else:
                        function = calculate_alpha(to_substitute, function, incoming)
                else:
                    function = calculate_alpha(to_substitute, function, incoming)

                new_function = function[:end_value].replace(to_substitute,incoming) + function[end_value:]
            else:
                new_function = calculate_alpha(to_substitute, function, incoming)
                new_function = new_function.replace(to_substitute,incoming)
        else:
            #If there's nothing to substitute, just rewrite the term in form
            #[?/x] and pass back up the tree
            substitution_form = "[?/"+to_substitute+"]"
            new_function = substitution_form + function
        
        print("Function after replacement in abstraction = "+new_function)
        #TODO: Implement proper typing here
        return new_function,function_type

    # Visit a parse tree produced by LambdaCalculusParser#function.
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):
        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            child_value,child_type = self.visit(ctx.getChild(1))
            return "" + ctx.getChild(0).getText() + child_value + ctx.getChild(2).getText(),child_type
        
        #NOTE: I should be calculating the function here and returning the result
        left,__ = self.visit(ctx.getChild(0))
        #TODO: Determine the typing rules here
        right,return_type = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()

        return_string = "" + left + op + right
        return return_string,return_type
        #return "" + self.visit(ctx.getChild(0)) + ctx.getChild(1).getText() + self.visit(ctx.getChild(2))

    # Visit a parse tree produced by LambdaCalculusParser#abstraction_term.
    def visitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        return self.visit(ctx.getChild(1))
        #return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#lambda_variable.
    def visitLambda_variable(self, ctx:LambdaCalculusParser.Lambda_variableContext):
        if ctx.getChild(2) is None:
            return ctx.getChild(0).getText(),None
        else:
            return ctx.getChild(0).getText(),ctx.getChild(2).getText()
        
        #return ctx.getChild(0).getText()
        #return ctx.getText()
    
    # Visit a parse tree produced by LambdaCalculusParser#variable.
    def visitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        if ctx.getChild(2) is None:
            return ctx.getChild(0).getText(),None
        else:
            return ctx.getChild(0).getText(),ctx.getChild(2).getText()
        
        #return ctx.getChild(0).getText()
        #return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#number.
    def visitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        if ctx.getChild(2) is None:
            return ctx.getChild(0).getText(),None
        else:
            return ctx.getChild(0).getText(),ctx.getChild(2).getText()

        #return ctx.getChild(0).getText()
        #return self.visitChildren(ctx)
    
    # Visit a parse tree produced by LambdaCalculusParser#operation.
    def visitOperation(self, ctx:LambdaCalculusParser.OperationContext):
        return self.visitChildren(ctx)
    
    
    # Visit a parse tree produced by LambdaCalculusParser#expression.
    def visitValue(self, ctx:LambdaCalculusParser.ValueContext):
        return self.visitChildren(ctx)
        #return ctx.getText()

    #NOTE: this absolutely definitely needs renamed
    def convert_back_abstraction_form(self, returned_abstraction):
        
        print("Returned abstraction = "+str(returned_abstraction))

        container_match = re.search("\[(.*?)\]", returned_abstraction)
        while container_match is not None:
            bound_match = re.search("\/(.*?)\]", returned_abstraction)
            found_bound = bound_match.group(1)
            container_to_replace = container_match.group(0)
            returned_abstraction = returned_abstraction.replace(container_to_replace,"%"+found_bound+".")
            container_match = re.search("\[(.*?)\]", returned_abstraction)
        
        return returned_abstraction