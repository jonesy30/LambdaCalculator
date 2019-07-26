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
        self.valid_typing = True

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

        #Get the tree created by the output of the left hand tree
        tree = self.create_tree(function)

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

        depth = ctx.depth()
        if depth == 1:
            
            #output,return_type = str(self.visitChildren(ctx))
            output,return_type = self.visitChildren(ctx)
            
            output,return_type = self.post_process(output, return_type)
            return output,return_type,self.valid_typing

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
        print("To substitute type on incoming = "+str(to_substitute_type))
        incoming_tuple = self.incoming_values.pop()
        print("Incoming tuple = "+str(incoming_tuple))

        incoming = None
        incoming_type = None
        
        if incoming_tuple == -1:
            incoming = incoming_tuple
        else:
            incoming = incoming_tuple[0]
            incoming_type = incoming_tuple[1]
        
        print("Incoming = "+str(incoming))

        print("Popped type = "+str(incoming_type))
        function,function_type = self.visit(ctx.getChild(2))

        print("To substitute = "+to_substitute)
        print("Function before abstraction = "+function)
        print("Incoming before abstraction = "+str(incoming))

        new_function = function
        if incoming != -1:
            bound_variables_left = re.findall("%(.*?)\.", function)
            subst_container_match = re.search("%(.*?)\.", function)
            
            if subst_container_match is not None:
                container = subst_container_match.group(0)

                end_value = len(function)
                if len(bound_variables_left) > 0:
                    #More than one bound variable -- do something here
                    if to_substitute in bound_variables_left:
                        #Bound variable repeated, need to check for the next instance of it
                        for i,letter in enumerate(function):
                            if letter == '%':
                                subst_container_match = re.search("%(.*?)\.", function[i:])
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
                print()
                print("To substitute type = "+str(to_substitute_type))
                print("To substitute = "+str(to_substitute))
                print("Incoming type = "+str(incoming_type))
                print()

                if to_substitute_type is not None:
                    to_substitute_type = to_substitute_type.lower()
                    if incoming_type is not None:
                        incoming_type = incoming_type.lower()
                        if to_substitute_type != incoming_type:
                            print()
                            print("Incoming type does not match specified input type")
                            print()
                            self.valid_typing = False

                if incoming_type is not None:
                    print("To substitute type is not none")
                    print(str(to_substitute_type))
                    incoming = incoming + ":" + incoming_type
                new_function = new_function.replace(to_substitute,incoming)

                print()
                print("New function before tree creation = "+str(new_function))
                print()
                tree = self.create_tree(new_function)

                new_function,function_type,valid_typing = self.visit(tree)

                if valid_typing == False:
                    self.valid_typing = False
                print()
                print("New function after tree creation = "+str(new_function))          
                print()  
        else:
            #If there's nothing to substitute, just rewrite the term in form
            #[?/x] and pass back up the tree
            print("To substitute = "+to_substitute)
            substitution_form = "%"+str(to_substitute)+":"+str(to_substitute_type)+"."
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
        left,left_type = self.visit(ctx.getChild(0))
        #TODO: Determine the typing rules here
        right,right_type = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()

        if left_type is not None:
            left_type = left_type.lower()
        
        if right_type is not None:
            right_type = right_type.lower()

        bool_bool = ["AND","OR"]
        int_int = ["+","-","*","/","^","EQ","GT","LT"]
        return_type = None

        if op in bool_bool:
            if left_type == "int" or right_type == "int":
                self.valid_typing = False
            elif self.valid_typing == True:
                return_type = "bool"
        elif op in int_int:
            if left_type == "bool" or right_type == "bool":
                self.valid_typing = False
            elif self.valid_typing == True:
                return_type = "int"
        
        #TODO: Do some actual calculations here
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
            print("In lambda variable "+ctx.getChild(0).getText())
            print("Type = "+ctx.getChild(2).getText())
            #return ctx.getChild(0).getText(),ctx.getChild(2).getText()
            return ctx.getChild(0).getText(),self.visit(ctx.getChild(2))
        
        #return ctx.getChild(0).getText()
        #return ctx.getText()
    
    # Visit a parse tree produced by LambdaCalculusParser#variable.
    def visitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        if ctx.getChild(2) is None:
            return ctx.getChild(0).getText(),None
        else:
            return ctx.getChild(0).getText(),self.visit(ctx.getChild(2))
        
        #return ctx.getChild(0).getText()
        #return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#number.
    def visitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        if ctx.getChild(2) is None:
            return ctx.getChild(0).getText(),None
        else:
            return ctx.getChild(0).getText(),self.visit(ctx.getChild(2))

        #return ctx.getChild(0).getText()
        #return self.visitChildren(ctx)
    
    # Visit a parse tree produced by LambdaCalculusParser#operation.
    def visitOperation(self, ctx:LambdaCalculusParser.OperationContext):
        return self.visitChildren(ctx)
    
    
    # Visit a parse tree produced by LambdaCalculusParser#expression.
    def visitValue(self, ctx:LambdaCalculusParser.ValueContext):
        return self.visitChildren(ctx)
        #return ctx.getText()
    
    # Visit a parse tree produced by LambdaCalculusParser#ground_type.
    def visitGround_type(self, ctx:LambdaCalculusParser.Ground_typeContext):
        return ctx.getText()
    
    # Visit a parse tree produced by LambdaCalculusParser#term_type.
    def visitTerm_type(self, ctx:LambdaCalculusParser.Term_typeContext):
        #child = self.visitChildren(ctx)
        #print("In term type: "+str(child))
        #return self.visitChildren(ctx)

        return self.visit(ctx.getChild(0))

        # if ctx.getChildCount() > 1:
        #     return self.visit(ctx.getChild(0)),self.visit(ctx.getChild(2))
        # else:
        #     return self.visit(ctx.getChild(0)),None

    def post_process(self, output, return_type):

        bad_strings = [":int",":Int",":INT",":bool",":Bool",":BOOL",":None",":NONE",":none"]

        output = str(output)
        return_type = str(return_type)
        for string in bad_strings:
            output = output.replace(string,"")

        return output,return_type

    def create_tree(self, function):
        stream = InputStream(function)
        lexer = LambdaCalculusLexer(stream)
        tokens = CommonTokenStream(lexer)
        parser = LambdaCalculusParser(tokens)
        tree = parser.term()

        return tree