from LambdaCalculusVisitor import LambdaCalculusVisitor
from AlphaCalculatorPartial import calculate_alpha
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
else:
    from LambdaCalculusParser import LambdaCalculusParser

class MyVisitor(LambdaCalculusVisitor):
    
    # Visit a parse tree produced by LambdaCalculusParser#application.
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        #print(self.visitChildren(ctx))
        #print("End of application")
        #print(self.visitChildren(ctx))
        self.visitChildren(ctx)
        
        #print("Child 0 = "+ctx.getChild(0).getText())
        #print("Child 1 = "+ctx.getChild(1).getChild(0).getText())
        #This could be useful?
        #print("Tree")
        #print(ctx.toStringTree())

        #bound variable at getChild(1).getChild(0)
        #function at getChild(1).getChild(2)
        #expression at getChild(3)

        [bound_variable, function] = self.visit(ctx.getChild(1))

        expression = ctx.getChild(3).getText()
        print("Expression before = "+expression)
        expression = calculate_alpha(bound_variable, function, expression)
        print("Expression after = "+expression)
        ##print("Bound variable through abstraction = "+str(bound_variable))
        ##print("Function through abstraction = "+str(function))
        ##print("Expression through abstraction = "+str(expression))

        new_function = function.replace(bound_variable,expression)
        ##print("New function = "+new_function)

        return new_function
        #return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#expression.
    def visitExpression(self, ctx:LambdaCalculusParser.ExpressionContext):
        return ctx.getText()

    # Visit a parse tree produced by LambdaCalculusParser#number.
    def visitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        #print("Number = "+ctx.getText())
        
        return self.visitChildren(ctx)
        #return "This is a number" + self.visitChildren(ctx)
    
    # Visit a parse tree produced by LambdaCalculusParser#term.
    def visitTerm(self, ctx:LambdaCalculusParser.TermContext):
        #return "Term = "+ctx.getText()
        #print("T: "+str(self.visitChildren(ctx)))
        #return self.visitChildren(ctx)
        
        # self.visitChildren(ctx)
        # if ctx.getChildCount() > 1:
        #     print("T: "+ctx.getChild(1))
        #     return ctx.getChild(1)
        # return None
        
        #print("Term me = "+ctx.getText())

        #This has stopped working for some reason
        # if self.visitChildren(ctx) is not None:
        #     [bound_variable, function] = self.visitChildren(ctx)
        #     print("Bound variable = "+bound_variable)
        #     return bound_variable
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        #print("In abstraction "+ctx.getText())
        #print("A: "+str(self.visitChildren(ctx)))  

        #Well that's interesting.... This gives %a as I want....
        #print("Child 0 = "+str(ctx.getChild(0).getText()))
        #print("Child 2 = "+str(ctx.getChild(2).getText()))

        #print("?? "+str(self.visitAbstraction_term(ctx)))
        #print("Number of children = "+str(ctx.getChildCount()))
        #return self.visitChildren(ctx)
        #return ctx.getChild(0).getText(), ctx.getChild(2).getText()
        #print("Child 0 = "+ctx.getChild(0).getText())
        #print("Child 1 = "+ctx.getChild(1).getText())
        #print("Child 2 = "+ctx.getChild(2).getText())
        #return ctx.getChild(0).getText(), ctx.getChild(2).getText()
        
        #Changing this to 0 returns %a
        #Changing this to 2 returns a+1
        #self.visitChildren(ctx)
        return self.visit(ctx.getChild(0)),ctx.getChild(2).getText()

    # Visit a parse tree produced by LambdaCalculusParser#function.
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):
        #left = self.visit(ctx.expression.getText())
        #print("Left = "+str(left))
        
        #right = self.visit(ctx.term(1))

        #print("Function = "+ctx.getText())
        #return self.visitChildren(ctx)
        return "F: "+ctx.getText()

        # Visit a parse tree produced by LambdaCalculusParser#abstraction_term.
    def visitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        #print("In abstraction term "+ctx.getText())
                
        #print("Children count = "+str(ctx.getChildCount()))
        #print("Children print = "+str(ctx.getChildren()))

        #This prints x
        #print(self.visitChildren(ctx))
        #This prints %x
        #print(self.visitLambda_variable(ctx))
        #print("End of children")
        #print("A_t: "+str(self.visitChildren(ctx)))
        #return self.visitLambda_variable(ctx)
        #print("Lambda term?" + self.visit(ctx.lambda_variable()))
        #print("A_t: "+str(self.visitChildren(ctx)))
        #return "A_t: "+str(self.visitChildren(ctx))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#lambda_variable.
    def visitLambda_variable(self, ctx:LambdaCalculusParser.Lambda_variableContext):
        #print("Printing lambda variable?")
        #print("Lambda variable = "+ctx.getText())
        
        #print("Lambda variable children:")
        #print(self.visitChildren(ctx))
        #print("End of lambda variable children")
        #return self.visitChildren(ctx)
        
        #I understand now. Because if I'm going straight to the lambda variable,
        #I'm not printing the lambda term, I'm printing the current context, which is me
        #Somehow I need to find a way to directly get to that lambda term
        # - maybe through the abstraction term?
        #print("Lambda = "+ctx.getText())
        
        #print("L? "+(str(ctx)))
        #print("L = "+ctx.getText())
        return ctx.getText()
        #return "L: "+ctx.getText()
    
#NOTE: doing ctx. gives a whole bunch of possible functions
    #well, it used to :(
#NOTE: self is MyVisitor (this seems obvious)