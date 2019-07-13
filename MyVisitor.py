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
        print("Original function = "+function)

        subst_container_match = re.search("\[(.*?)\]", function)
        container = subst_container_match.group(0)
        function = function.replace(container,"",1)
        print("Function after extracton + "+function)

        bound_variable_match = re.search("/(.*?)\]", container)
        bound_variable = bound_variable_match.group(1)

        #get all bound variables found in [?/bound_variable]function
        #bound_variable = re.findall("/(.*?)\]", function)
        #match = re.search("/(.*?)\]", function)
        #get the first group (the inner bit of the regex) which matches this expression -- outermost first
        #bound_variable = match.group(1)
        #NOTE: I need to find a way of only getting rid of the first bit
        #function = re.sub("\[(.*?)\]","",function)

        print("Bound variable = "+bound_variable)

        print("Function after = "+str(function))
        expression = ctx.getChild(1).getText()
        ##print("Function before = "+function)
        function = calculate_alpha(bound_variable,function, expression)
        ##print("Function after = "+function)
        print("Bound variable through abstraction = "+str(bound_variable))
        print("Function through abstraction = "+str(function))
        print("Expression through abstraction = "+str(expression))

        new_function = function.replace(bound_variable,expression)
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