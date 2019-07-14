from LambdaCalculusVisitor import LambdaCalculusVisitor
from AlphaCalculatorPartial import calculate_alpha
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
else:
    from LambdaCalculusParser import LambdaCalculusParser
import re

class MyVisitor(LambdaCalculusVisitor):
    
    # Visit a parse tree produced by LambdaCalculusParser#application.
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        print("In application "+ctx.getText())
        self.visitChildren(ctx)

        function = self.visit(ctx.getChild(0))
        expression = ctx.getChild(1).getText()
 
        print("Before function = "+function)

        bound_variables_left = re.findall("/(.*?)\]", function)

        subst_container_match = re.search("\[(.*?)\]", function)
        container = subst_container_match.group(0)
        function = function.replace(container,"",1)

        to_substitute = bound_variables_left[0]
        bound_variables_left.pop(0)

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
                function = calculate_alpha(to_substitute, function, expression, 0, end_value)
            else:
                function = calculate_alpha(to_substitute, function, expression)
        else:
            function = calculate_alpha(to_substitute, function, expression)

        new_function = function[:end_value].replace(to_substitute,expression) + function[end_value:]
        print("New function = "+new_function)
        
        return new_function

    # Visit a parse tree produced by LambdaCalculusParser#expression.
    def visitValue(self, ctx:LambdaCalculusParser.ValueContext):
        return ctx.getText()

    # Visit a parse tree produced by LambdaCalculusParser#parenthesis.
    def visitParenthesis(self, ctx:LambdaCalculusParser.ParenthesisContext):
        return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()

    # Visit a parse tree produced by LambdaCalculusParser#number.
    def visitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by LambdaCalculusParser#term.
    def visitTerm(self, ctx:LambdaCalculusParser.TermContext):
        ##print("T: "+ctx.getText())

        depth = ctx.depth()
        if depth == 1:
            print("Terminal node detected")
            output = str(self.visitChildren(ctx))
            container_match = re.search("\[(.*?)\]", output)

            print("old function = "+output)
            while container_match is not None:
                print("FOUND BOUND! ")
                bound_match = re.search("\/(.*?)\]", output)
                found_bound = bound_match.group(1)
                container_to_replace = container_match.group(0)
                print("To replace = "+container_to_replace)
                output = output.replace(container_to_replace,"%"+found_bound+".")
                container_match = re.search("\[(.*?)\]", output)
            
            print("New function = "+output)
            return output

        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        ##print()
        ##print("A: "+ctx.getText())

        bound_variable = self.visit(ctx.getChild(0))
        function = self.visit(ctx.getChild(2))

        ##print("Bound variable = "+bound_variable)
        ##print("Function = "+function)
        ##print()

        substitution_form = "[?/"+bound_variable+"]"
        ##print("Substitution form = "+substitution_form)
        modified_function = substitution_form + function
        ##print("New function = "+modified_function)

        return modified_function

    # Visit a parse tree produced by LambdaCalculusParser#function.
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):
        #self.visitChildren(ctx)
        ##print("F: "+ctx.getText())
        
        #NOTE: I should be calculating the function here and returning the result
        return "" + self.visit(ctx.getChild(0)) + ctx.getChild(1).getText() + self.visit(ctx.getChild(2))

        # Visit a parse tree produced by LambdaCalculusParser#abstraction_term.
    def visitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        #print("Children count = "+str(ctx.getChildCount()))
        #print("Children print = "+str(ctx.getChildren()))

        #This prints x
        #print(self.visitChildren(ctx))
        #This prints %x
        #print(self.visitLambda_variable(ctx))
        
        ##print("A_t: "+ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#lambda_variable.
    def visitLambda_variable(self, ctx:LambdaCalculusParser.Lambda_variableContext):
        return ctx.getText()
    
#NOTE: doing ctx. gives a whole bunch of possible functions
    #well, it used to :(
#NOTE: self is MyVisitor (this seems obvious)
#NOTE: Just always visit children, even if you don't need to, what's the harm?
#NOTE: This could be useful?
    #print("Tree")
    #print(ctx.toStringTree())