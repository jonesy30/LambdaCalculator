from LambdaCalculusVisitor import LambdaCalculusVisitor
from AlphaCalculatorPartial import calculate_alpha
from Stack import Stack
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
else:
    from LambdaCalculusParser import LambdaCalculusParser
import re

class MyLambdaVisitor(LambdaCalculusVisitor):
    
    ##Normal order reduction idea:
    #For application, get function and incoming expression from children and substitute
    #If there is still redexes left in the expression, visit corresponding children
    #This supports my use of visitors and not listeners

    def __init__(self):
        super()
        self.incoming_values = Stack() #This definitely needs renamed

    # Visit a parse tree produced by LambdaCalculusParser#application.
    def visitApplication(self, ctx:LambdaCalculusParser.ApplicationContext):
        
        print("Application = "+ctx.getText())

        expression = ctx.getChild(1).getText()
        self.incoming_values.push(expression) #NOTE: what if a non-evaluator?

        before_size = self.incoming_values.get_size()
        print("Stack size before = "+str(before_size))
        function = self.visit(ctx.getChild(0))
        after_size = self.incoming_values.get_size()
        print("Stack size after = "+str(after_size))

        #self.visitChildren(ctx)
        # if isinstance(ctx.getChild(0),LambdaCalculusParser.ParenthesisContext):
        #     print("Abstraction found!!")
        #     print("This could be useful....")
        #     self.visitParenthesis(ctx.getChild(0),"Hello message")
        # else:
        #     print("Well that didn't work as I predicted")
        # print(str(type(ctx.getChild(0))))

        print("Function_in_application = "+function)
        print("Expression_in_application = "+expression)
        #bound_variables_left = re.findall("/(.*?)\]", function)

        #subst_container_match = re.search("\[(.*?)\]", function)
        
        # if subst_container_match is not None:
        #     print("   Match")
        #     container = subst_container_match.group(0)
        #     function = function.replace(container,"",1)
        #     print("Function after replacement = "+function)
        #     to_substitute = bound_variables_left[0]
        #     bound_variables_left.pop(0)

        #     end_value = len(function)
        #     if len(bound_variables_left) > 0:
        #         #More than one bound variable -- do something here
        #         if to_substitute in bound_variables_left:
        #             #Bound variable repeated, need to check for the next instance of it
        #             for i,letter in enumerate(function):
        #                 if letter == '[':
        #                     subst_container_match = re.search("/(.*?)\]", function[i:])
        #                     bound_value = subst_container_match.group(1)
        #                     if to_substitute == bound_value:
        #                         break
        #             end_value = i
        #             function = calculate_alpha(to_substitute, function, expression, 0, end_value)
        #         else:
        #             function = calculate_alpha(to_substitute, function, expression)
        #     else:
        #         function = calculate_alpha(to_substitute, function, expression)

        #     new_function = function[:end_value].replace(to_substitute,expression) + function[end_value:]
        # else:
        #     #new_function = self.visitChildren(ctx)
        #     new_function = self.visit(ctx.getChild(0)) + self.visit(ctx.getChild(1))

        #return new_function
        
        ###This section is just a test -- will be removed (right future Yola????)
        #I also need to be careful not to visit children too much
        #self.visitChildren(ctx)
        #function = self.visit(ctx.getChild(0))
        #print("New function in application = "+function)

        #return self.visitChildren(ctx)
        #Ok, this definitely needs to be cleaned up to return something else, but that's progress at least
       
        #yeah, this is in no way correct
        #Two solutions that I can see:
            #Rewrite the grammar so LBRACKET abstraction RBRACKET is registered as an abstraction, and check whether the right subtree
            #is an abstraction
        #OR
            #Check the size of the stack before and after to see whether the value has been used
        
        returned_function = function
        if before_size == after_size:
            returned_function = function + expression
            self.incoming_values.pop()

        print("Returned value in application = "+returned_function)
        return returned_function

    # Visit a parse tree produced by LambdaCalculusParser#expression.
    def visitValue(self, ctx:LambdaCalculusParser.ValueContext):
        return ctx.getText()

    # Visit a parse tree produced by LambdaCalculusParser#parenthesis.
    def visitParenthesis(self, ctx:LambdaCalculusParser.ParenthesisContext):
        #Label
        print("P: "+ctx.getText())
        visit_children = self.visit(ctx.getChild(1))
        print("Parenthesis visit = "+visit_children)
        return "" + ctx.getChild(0).getText() + visit_children + ctx.getChild(2).getText()

        #return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()

    # Visit a parse tree produced by LambdaCalculusParser#number.
    def visitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by LambdaCalculusParser#term.
    def visitTerm(self, ctx:LambdaCalculusParser.TermContext):
        print("T: "+ctx.getText())

        #The abstraction puts lambda terms into [?/x] form, this chunk of code just converts it back before it gets
        #passed to the user for readability
        depth = ctx.depth()
        if depth == 1:
            output = str(self.visitChildren(ctx))
            container_match = re.search("\[(.*?)\]", output)

            while container_match is not None:
                bound_match = re.search("\/(.*?)\]", output)
                found_bound = bound_match.group(1)
                container_to_replace = container_match.group(0)
                output = output.replace(container_to_replace,"%"+found_bound+".")
                container_match = re.search("\[(.*?)\]", output)
            
            return output

        else:
            visit_children = self.visitChildren(ctx)
            print("Term visit = "+visit_children)
            return visit_children
            #return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        ##print()
        ##print("Incoming = "+str(self.incoming_values.pop()))
        print("Abstraction = "+ctx.getText())

        bound_variable = self.visit(ctx.getChild(0))
        function = self.visit(ctx.getChild(2))

        incoming = self.incoming_values.pop()

        new_function = function
        if incoming != -1:
            new_function = function.replace(bound_variable,incoming)
        else:
            substitution_form = "[?/"+bound_variable+"]"
            new_function = substitution_form + function

        print("Bound variable in abstraction = "+bound_variable)
        print("Function in abstraction = "+function)
        ##print()

        
        print("New function in abstraction = "+new_function)
        return new_function

    # Visit a parse tree produced by LambdaCalculusParser#function.
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):
        #self.visitChildren(ctx)
        print("F: "+ctx.getText())
        
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