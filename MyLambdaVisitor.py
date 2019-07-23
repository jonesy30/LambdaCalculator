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

        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()

        #NOTE: I need to evaluate the second tree
        #expression = ctx.getChild(1).getText()
        #self.incoming_values.push(expression) 

        #before_size = self.incoming_values.get_size()
        function = self.visit(ctx.getChild(0))
        expression = self.visit(ctx.getChild(1))

        print("In application, function = "+str(function))
        print("In application, expression = "+str(expression))

        #NOTE: I definitely don't need to change form any more
        function = self.convert_back_abstraction_form(function)
        expression = self.convert_back_abstraction_form(expression)
        #after_size = self.incoming_values.get_size()

        # returned_function = function
        # if before_size == after_size:
        #     returned_function = function + expression
        #     self.incoming_values.pop()

        #Get the tree created by the output of the left hand tree

        stream = InputStream(function)
        lexer = LambdaCalculusLexer(stream)
        tokens = CommonTokenStream(lexer)
        parser = LambdaCalculusParser(tokens)
        tree = parser.term()

        #Find the type of the first root node (ignoring terms)
        am_I_an_abstraction = tree
        while isinstance(am_I_an_abstraction,LambdaCalculusParser.TermContext):
            print("Term found, get child")
            print("Term in tree = "+str(type(am_I_an_abstraction)))
            am_I_an_abstraction = am_I_an_abstraction.getChild(0)

        print("Term in tree = "+str(type(am_I_an_abstraction)))
        #This (it might be only one getChild(0)) will tell me the tpe of the returned M
        #And therefore whether I need to do more to it to get the final value
        if isinstance(am_I_an_abstraction,LambdaCalculusParser.AbstractionContext):
            print("I am not done here - pushing and visiting")
            self.incoming_values.push(expression)
            function = self.visit(am_I_an_abstraction)
        else:
            function = function + expression
            print("I am done here, adding expression to function")

        print("Returned value in application = "+function)
        return function

    # Visit a parse tree produced by LambdaCalculusParser#expression.
    def visitValue(self, ctx:LambdaCalculusParser.ValueContext):
        return ctx.getText()

    # Visit a parse tree produced by LambdaCalculusParser#parenthesis.
    # def visitParenthesis(self, ctx:LambdaCalculusParser.ParenthesisContext):
    #     #Label
    #     #print("P: "+ctx.getText())
    #     visit_children = self.visit(ctx.getChild(1))
    #     return "" + ctx.getChild(0).getText() + visit_children + ctx.getChild(2).getText()

    #     #return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()

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
            #NOTE: do I need this in here if I'm just doing the same thing in the abstraction? Or should I just get rid of this
            #string manipulation altogether?
            print("In term, output is = "+str(output))
            output = self.convert_back_abstraction_form(output)            
            return output

        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        print("Abstraction = "+ctx.getText())

        #Pop the value as soon as you get the abstraction term, before you
        #visit the rest of the children, so the correct term gets associated
        #with the correct input

        #to_substitute = self.visit(ctx.getChild(0))
        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()
        
        to_substitute = self.visit(ctx.getChild(0))
        incoming = self.incoming_values.pop()
        function = self.visit(ctx.getChild(2))

        print("To subsitute = "+to_substitute)
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
        return new_function

    # Visit a parse tree produced by LambdaCalculusParser#function.
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):
        print("F: "+ctx.getText())

        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            return "" + ctx.getChild(0).getText() + self.visit(ctx.getChild(1)) + ctx.getChild(2).getText()
        
        #NOTE: I should be calculating the function here and returning the result
        return "" + self.visit(ctx.getChild(0)) + ctx.getChild(1).getText() + self.visit(ctx.getChild(2))

    # Visit a parse tree produced by LambdaCalculusParser#abstraction_term.
    def visitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#lambda_variable.
    def visitLambda_variable(self, ctx:LambdaCalculusParser.Lambda_variableContext):
        return ctx.getText()

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

    
#NOTE: doing ctx. gives a whole bunch of possible functions
    #well, it used to :(
#NOTE: self is MyVisitor (this seems obvious)
#NOTE: Just always visit children, even if you don't need to, what's the harm?
#NOTE: This could be useful?
    #print("Tree")
    #print(ctx.toStringTree())
    #to print children: ctx.getChildren()
    #to print number of children: ctx.getChildCount()