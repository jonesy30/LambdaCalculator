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

class BaseVisitor(LambdaCalculusVisitor):

    def __init__(self):
        super()
    
    # Visit a parse tree produced by LambdaCalculusParser#term.
    def visitTerm(self, ctx:LambdaCalculusParser.TermContext):
        print("T: "+ctx.getText())

        depth = ctx.depth()
        if depth == 1:
            
            output = None
            return_type = None

            output_tuple = self.visitChildren(ctx)
            if output_tuple is not None:
                output = output_tuple[0]
                return_type = output_tuple[1]

            output,return_type = self.post_process(output, return_type)
            return output,return_type,self.valid_typing

        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#function.
    #NOTE: having function_type = None could be a way to fix my "invalid typing when bound variable does not match inner variable" issue
    #Just call this method directly from the abstraction term if the thing below is a function
    #NOTE: If I don't end up needing this, take it out!
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):

        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            child_value,child_type,input_type = self.visit(ctx.getChild(1))
            return "" + ctx.getChild(0).getText() + child_value + ctx.getChild(2).getText(),child_type,input_type
        
        #NOTE: I should be calculating the function here and returning the result
        returned_left = self.visit(ctx.getChild(0))

        left = returned_left[0]
        left_type = returned_left[1]

        returned_right = self.visit(ctx.getChild(2))
        
        right = returned_right[0]
        right_type = returned_right[1]

        op = ctx.getChild(1).getText()

        if left_type is not None:
            left_type = left_type.lower()
        
        if right_type is not None:
            right_type = right_type.lower()

        print("Left = "+left)
        print("Right = "+right)


        #Functions that take two booleans and return a boolean
        bool_bool = ["&","|"]
        #Take two ints and return an int
        int_int = ["+","-","*","/","^"]
        #Takes two ints and returns a boolean
        int_bool = ["==",">","<"]
        return_type = None
        input_type = None

        if op in bool_bool:
            if left_type == "int" or right_type == "int":
                self.set_valid_typing(False)
            elif self.valid_typing == True:
                return_type = "bool"
                input_type = "bool"
        elif op in int_int:
            if left_type == "bool" or right_type == "bool":
                self.set_valid_typing(False)
            elif self.valid_typing == True:
                return_type = "int"
                input_type="int"
        elif op in int_bool:
            if left_type == "bool" or right_type == "bool":
                self.set_valid_typing(False)
            elif self.valid_typing == True:
                return_type = "bool"
                input_type = "int"

        #If the input type is a function we can't work out what the input type is
        #NOTE: THIS IS A LIMITATION
        if isinstance(ctx.getChild(0),LambdaCalculusParser.FunctionContext) or isinstance(ctx.getChild(2),LambdaCalculusParser.FunctionContext):
            input_type = None
        
        #TODO: Do some actual calculations here
        return_string = "" + left + op + right
        
        print("Me = "+ctx.getText())
        print("Returning input type = "+str(input_type))
        return return_string,return_type,input_type
    
    # Visit a parse tree produced by LambdaCalculusParser#variable.
    def visitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        if ctx.getChild(2) is None:
            return ctx.getChild(0).getText(),None
        else:
            return ctx.getChild(0).getText(),self.visit(ctx.getChild(2))

    # Visit a parse tree produced by LambdaCalculusParser#abstraction_term.
    def visitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        return self.visit(ctx.getChild(1))
        #return self.visitChildren(ctx)
        
    # Visit a parse tree produced by LambdaCalculusParser#number.
    def visitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        return ctx.getChild(0).getText(),"int"

    # Visit a parse tree produced by LambdaCalculusParser#boolean_value.
    def visitBoolean_value(self, ctx:LambdaCalculusParser.Boolean_valueContext):
        return ctx.getChild(0).getText(),"bool"
    
    # Visit a parse tree produced by LambdaCalculusParser#operation.
    def visitOperation(self, ctx:LambdaCalculusParser.OperationContext):
        return self.visitChildren(ctx)
    
    
    # Visit a parse tree produced by LambdaCalculusParser#expression.
    def visitValue(self, ctx:LambdaCalculusParser.ValueContext):
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by LambdaCalculusParser#term_type.
    def visitFunction_type(self, ctx:LambdaCalculusParser.Function_typeContext):
        return ctx.getText()

    #NOTE: Please rename this future Yola...
    def convert_function_with_type(self, to_substitute, to_substitute_type, incoming, incoming_type, function, end_value=None):

        #If there is a bound variable type to be substituted, add it to the rest of the bound variables in the term
        if to_substitute_type is not None:
            incoming = incoming + ":" + to_substitute_type

            if end_value is not None:
                function = function[:end_value].replace(to_substitute,incoming) + function[end_value:]
            else:
                function = function.replace(to_substitute,incoming)
        
        #If the substituted type is none but the incoming type is not, we still know what the bound variable type should now be, so replace it
        elif incoming_type is not None:
            incoming = incoming + ":" + incoming_type

            if end_value is not None:
                function = function[:end_value].replace(to_substitute,incoming) + function[end_value:]
            else:
                function = function.replace(to_substitute,incoming)
            
        return function

    def type_check_application(self, function_type, expression_type):
        #Type check the application
        application_type_journey = []

        print("I am in type check application")
        print("Function type = "+str(function_type))
        print("Expression type = "+str(expression_type))
        if function_type is not None:
            #Split the type of the function term into their journeys (1 -> 2 -> 3 -> ...n)
            function_type_journey = function_type.split("->")
            if expression_type is not None:
                #Do the same splitting with the type of the expression
                expression_type_journey = expression_type.split("->")
                application_type_journey = []

                #Check whether the typing is valid or not
                if len(function_type_journey) > len(expression_type_journey):
                    type_mismatch = False
                    while len(expression_type_journey) > 0:
                        if function_type_journey[0] != expression_type_journey[0]:
                            function_journey_step = function_type_journey[0].lower()
                            expression_journey_step = expression_type_journey[0].lower()
                            if function_journey_step == "none" or expression_journey_step == "none":
                                #NOTE: Repeated code
                                del function_type_journey[0]
                                del expression_type_journey[0]
                            else:
                                expression_type_journey = []
                                type_mismatch = True
                        else:
                            del function_type_journey[0]
                            del expression_type_journey[0]
                    if type_mismatch == False:
                        application_type_journey = function_type_journey
                    else:
                        self.set_valid_typing(False)
            else:
                print("Function type journey = "+str(function_type_journey))
                del function_type_journey[0]
                application_type_journey = function_type_journey
    
        if application_type_journey == [] or application_type_journey == None:
            application_type = "None"
        else:
            #Create the abstraction type string based on what's left of the function type term
            print("Application_type_journey = "+str(application_type_journey))
            application_type = ""
            for i,journey_step in enumerate(application_type_journey):
                application_type = application_type + "->" + application_type_journey[i]
            application_type=application_type[2:]
    
        return application_type

    def add_bound_variable_types_to_function(self, bound_variable, function, type):
        if type is None:
            type = "none"
        
        function_list = list(function)
        for i,character in enumerate(function_list):
            if character == bound_variable:
                function_list[i] = character + ":" + type

        processed_function = "".join(function_list)
        return processed_function

    def convert_type_if_none(self, term_type):
        
        if term_type is not None:
            term_type = term_type.lower()
            if term_type == "none":
                term_type = None
            
        return term_type

    def post_process(self, output, return_type):

        bad_strings = [":int",":Int",":INT",":bool",":Bool",":BOOL",":None",":NONE",":none"]

        output = str(output)
        return_type = str(return_type)
        for string in bad_strings:
            output = output.replace(string,"")

        return output,return_type

    def create_tree(self, function):
        if function is not None:
            stream = InputStream(function)
            lexer = LambdaCalculusLexer(stream)
            tokens = CommonTokenStream(lexer)
            parser = LambdaCalculusParser(tokens)
            tree = parser.term()

            return tree

    def check_for_parenthesis(self, ctx):
        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            child_value,child_type = self.visit(ctx.getChild(1))
            return "" + ctx.getChild(0).getText() + child_value + ctx.getChild(2).getText(),child_type
        else:
            return -1
    
    def perform_abstraction(self, ctx, incoming, incoming_type, to_substitute, to_substitute_type):
        
        #If the types of the substituted or incoming values are the string "none" (or any capitalised version of none)
        #set it to standard value None (makes type checking and setting easier later)
        incoming_type = self.convert_type_if_none(incoming_type)
        to_substitute_type = self.convert_type_if_none(to_substitute_type)

        #Visit and evaluate the right hand side child (the function)
        returned_child = self.visit(ctx.getChild(2))
        function = returned_child[0]
        function_type = returned_child[1]

        input_type = None
        if len(returned_child) == 3:
            input_type = returned_child[2]
        
        if to_substitute_type == None:
            to_substitute_type = input_type

        print("To substitute = "+to_substitute)
        print("Function before abstraction = "+function)
        print("Incoming before abstraction = "+str(incoming))

        new_function = self.add_bound_variable_types_to_function(to_substitute,function,to_substitute_type)
        #new_function = function

        #If there is a value to subsitute into this abstraction
        if incoming != -1:
            bound_variables_left = re.findall("%(.*?)\.", function)
            subst_container_match = re.search("%(.*?)\.", function)
            
            if subst_container_match is not None:
                container = subst_container_match.group(0)

                end_value = len(function)
                #If there is more than zero bound variables found in the string
                if len(bound_variables_left) > 0:
                    for i,bound_variable in enumerate(bound_variables_left):
                        type_match = re.search(":(.*)", bound_variable)
                        bound_variables_left[i] = bound_variable.replace(type_match.group(0),"")

                    #More than one bound variable - check whether they match the current bound variable
                    if to_substitute in bound_variables_left:
                        #Bound variable repeated, need to check for the next instance of it and stop evaluating there
                        for i,letter in enumerate(function):
                            if letter == '%':
                                subst_container_match = re.search("%(.*?)\.", function[i:])
                                bound_value = subst_container_match.group(1)
                                type_match = re.search(":(.*)", bound_variable)
                                bound_value = bound_value.replace(type_match.group(0),"")
                                if to_substitute == bound_value:
                                    break
                        end_value = i
                        function = calculate_alpha(to_substitute, function, incoming, 0, end_value)
                    
                    #If there is not more than one of the same bound variable detected, just alpha convert as normal
                    else:
                        function = calculate_alpha(to_substitute, function, incoming)
                
                #If there are no bound variables inside the string found, alpha convert as normal
                else:
                    function = calculate_alpha(to_substitute, function, incoming)

                #Replace the bound variables with the incoming value, up until the end point (the point where there's bound variable crossover)
                print("New function at checkpoint marker 1 = "+new_function[:end_value])

                #Convert the new function to include the types from either the bound value or the incoming value (depending on which has a type)
                new_function = self.convert_function_with_type(to_substitute, to_substitute_type, incoming, incoming_type, new_function, end_value)
                #Replace the bound variable with the new incoming value
                new_function = function[:end_value].replace(to_substitute,incoming) + function[end_value:]

            #If there are no other lambda terms found within the current lambda term
            else:
                #Calculate the alpha reduction as normal
                new_function = calculate_alpha(to_substitute, function, incoming)
                #Convert the new function to include the types from either the bound value or the incoming value (depending on which has a type)
                new_function = self.convert_function_with_type(to_substitute, to_substitute_type, incoming, incoming_type, new_function)
                #Replace the bound variable with the new incoming value
                new_function = new_function.replace(to_substitute,incoming)

            print("New function at checkpoint marker 2 = "+new_function)
            print()
            print("To substitute type = "+str(to_substitute_type))
            print("To substitute = "+str(to_substitute))
            print("Incoming type = "+str(incoming_type))
            print()

            #Check valid/invalid type by comparing the incoming type to the bound variable type
            if to_substitute_type is not None:
                to_substitute_type_journey = to_substitute_type.split("->")
                if incoming_type is not None:
                    incoming_type_journey = incoming_type.split("->")
                    if to_substitute_type_journey[0] != incoming_type_journey[0]:
                        #self.valid_typing = False
                        self.set_valid_typing(False)

            print()
            print("New function before tree creation = "+str(new_function))
            print()

            #Create a tree of the result of the inner function, and evaluate it
            tree = self.create_tree(new_function)
            new_function,function_type,valid_typing = self.visit(tree)

            if valid_typing == False:
                self.set_valid_typing(False)

            print()
            print("New function after tree creation = "+str(new_function))          
            print()  
            print("Incoming, incoming type = "+str(incoming_type))
        
        #If there is not a value to substitute into this abstraction
        else:
            #Create a tree of the result of the inner function, and evaluate it
            tree = self.create_tree(new_function)
            new_function,function_type,valid_typing = self.visit(tree)

            if valid_typing == False:
                self.set_valid_typing(False)

            #If there's nothing to do here, just convert back to %x.M form
            #and pass the value back up the tree, adding the types back in
            if to_substitute_type is not None:
                substitution_form = "%"+str(to_substitute)+":"+str(to_substitute_type)+"."
            else:
                substitution_form = "%"+str(to_substitute)+"."
            new_function = substitution_form + function
        
        #Create the new abstraction type, which is the bound variable type -> the type it gets converted to
        abstraction_type = str(to_substitute_type) + "->" + str(function_type)
        print("Function after replacement in abstraction = "+new_function)
        print("Abstraction type = "+str(abstraction_type))

        return new_function, abstraction_type

    def set_valid_typing(self,result):
        if self.valid_typing == True:
            self.valid_typing = result
