from LambdaCalculusVisitor import LambdaCalculusVisitor
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
else:
    from LambdaCalculusParser import LambdaCalculusParser

class MyVisitor(LambdaCalculusVisitor):
    
    # Visit a parse tree produced by LambdaCalculusParser#application.
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        print("In an application "+ctx.getText())
        print(self.visitChildren(ctx))
        print("End of application")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#number.
    def visitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        #print("Number = "+ctx.getText())
        
        return self.visitChildren(ctx)
        #return "This is a number" + self.visitChildren(ctx)
    
    # Visit a parse tree produced by LambdaCalculusParser#term.
    def visitTerm(self, ctx:LambdaCalculusParser.TermContext):
        #print("Term = "+ctx.getText())
        #return "Term = "+ctx.getText()
        print("T: "+str(self.visitChildren(ctx)))
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        print("In abstraction "+ctx.getText())
        print("A: "+str(self.visitChildren(ctx)))  

        #Well that's interesting.... This gives %a as I want....
        print("Child = "+str(ctx.getChild(0).getText()))
        
        #print("?? "+str(self.visitAbstraction_term(ctx)))
        print("Number of children = "+str(ctx.getChildCount()))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#function.
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):
        #left = self.visit(ctx.expression.getText())
        #print("Left = "+str(left))
        
        #right = self.visit(ctx.term(1))

        print("Function = "+ctx.getText())
        #return self.visitChildren(ctx)
        #return "F: "+ctx.getText()

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
        print("A_t: "+str(self.visitChildren(ctx)))
        #return self.visitLambda_variable(ctx)
        #print("Lambda term?" + self.visit(ctx.lambda_variable()))
        return "A_t: "+str(self.visitChildren(ctx))
        #return "A_t: "+str(self.visitLambda_variable(ctx))

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
        return "L: "+ctx.getText()
    
#NOTE: doing ctx. gives a whole bunch of possible functions