from LambdaCalculusVisitor import LambdaCalculusVisitor
from LambdaErrorListener import LambdaErrorListener, SyntaxTokenError
from antlr4.error.Errors import NoViableAltException
from AlphaCalculatorPartial import calculate_alpha
from Stack import Stack
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaCalculusParser import LambdaCalculusParser
    from .LambdaCalculusLexer import LambdaCalculusLexer
else:
    from LambdaCalculusParser import LambdaCalculusParser
    from LambdaCalculusLexer import LambdaCalculusLexer
from LambdaSessionInformationObject import LambdaSessionInformationObject
import re

class BaseVisitor(LambdaCalculusVisitor):

    def __init__(self):
        super()
        self.final_result = ""

    def __del__(self):
        self.session_object.add_beta_step("Final result = "+str(self.final_result))
    
    # Visit a parse tree produced by LambdaCalculusParser#term.
    def visitTerm(self, ctx:LambdaCalculusParser.TermContext):
        depth = ctx.depth()
        if depth == 1:
            
            output = None
            return_type = None

            output_tuple = self.visitChildren(ctx)
            if output_tuple == -1:
                return -1
            elif output_tuple is not None:
                output = output_tuple[0]
                return_type = output_tuple[1]

            self.send_current_to_super_context()

            self.post_process_contexts()
            self.send_context_to_session()

            self.final_result = output
            return output,return_type,self.valid_typing

        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#function.
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):

        #print("Function = "+ctx.getText())

        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            child_value,child_type,input_type = self.visit(ctx.getChild(1))
            return "" + ctx.getChild(0).getText() + child_value + ctx.getChild(2).getText(),child_type,input_type
        
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
        if isinstance(ctx.getChild(0),LambdaCalculusParser.FunctionContext) or isinstance(ctx.getChild(2),LambdaCalculusParser.FunctionContext):
            input_type = None

        return_string = "" + left + op + right

        #If left and right are letters which aren't TRUE or FALSE
        if left.isalpha() and len(left)<2:
            self.add_variable_to_context(left,input_type)
        if right.isalpha() and len(right)<2:
            self.add_variable_to_context(right,input_type)
        
        return return_string,return_type,input_type
    
    # Visit a parse tree produced by LambdaCalculusParser#variable.
    def visitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        variable = (ctx.getChild(0)).getText()

        if ctx.getChild(2) is None:
            return ctx.getText(),None
        else:
            variable_type = self.visit(ctx.getChild(2))
            self.add_variable_to_context(variable, variable_type)

            return ctx.getText(),variable_type

    # Visit a parse tree produced by LambdaCalculusParser#abstraction_term.
    def visitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        return self.visit(ctx.getChild(1))
        
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

        new_end_value = end_value
        #If there is a bound variable type to be substituted, add it to the rest of the bound variables in the term
        if to_substitute_type is not None:
            if ":" not in incoming:
                incoming = incoming + ":" + to_substitute_type

            if end_value is not None:
                new_function = function[:end_value].replace(to_substitute,incoming)
                new_end_value = len(new_function)
                function = new_function + function[end_value:]
            else:
                function = function.replace(to_substitute,incoming)
                
        #If the substituted type is none but the incoming type is not, we still know what the bound variable type should now be, so replace it
        elif incoming_type is not None:
            if ":" not in incoming:
                incoming = incoming + ":" + incoming_type

            if end_value is not None:
                new_function = function[:end_value].replace(to_substitute,incoming)
                new_end_value = len(new_function)
                function = new_function + function[end_value:]
            else:
                function = function.replace(to_substitute,incoming)

        return function,new_end_value

    def type_check_application(self, function_type, expression_type):
        #Type check the application
        application_type_journey = []

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
                del function_type_journey[0]
                application_type_journey = function_type_journey
    
        if application_type_journey == [] or application_type_journey == None:
            application_type = "None"
        else:
            #Create the abstraction type string based on what's left of the function type term
            application_type = ""
            for i,journey_step in enumerate(application_type_journey):
                application_type = application_type + "->" + application_type_journey[i]
            application_type=application_type[2:]
    
        return application_type

    def add_bound_variable_types_to_function(self, bound_variable, function, type):
        
        if ":" in bound_variable:
            head, sep, tail = bound_variable.partition(':')
            bound_variable = head

        if type is not None:
            function_list = list(function)
            function_list.append(" ")
            for i,character in enumerate(function_list):
                if character == bound_variable:
                    if function_list[i+1] != ":":
                        function_list[i] = character + ":" + type

            processed_function = "".join(function_list)
            
            return processed_function
        else:
            return function

    def convert_type_if_none(self, term_type):
        
        if term_type is not None:
            term_type = term_type.lower()
            if term_type == "none":
                term_type = None
            
        return term_type

    def create_tree(self, function):
        if function is not None:
            stream = InputStream(function)
            lexer = LambdaCalculusLexer(stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(LambdaErrorListener())
            tokens = CommonTokenStream(lexer)
            parser = LambdaCalculusParser(tokens)
            tree = parser.term()

            return tree

    def check_for_parenthesis(self, ctx):
        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            child_value,child_type = self.visit(ctx.getChild(1))
            return "" + ctx.getChild(0).getText() + str(child_value) + ctx.getChild(2).getText(),child_type
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

        function = self.add_bound_variable_types_to_function(to_substitute,function,to_substitute_type)
        new_function = function

        #If there is a value to subsitute into this abstraction
        if incoming != -1:
            bound_variables_left = re.findall("%(.*?)\.", function)
            subst_container_match = re.search("%(.*?)\.", function)
            
            #If there is bound variables left inside the function
            if subst_container_match is not None:
                container = subst_container_match.group(0)

                end_value = len(function)
                #If there is more than zero bound variables found in the string
                if len(bound_variables_left) > 0:
                    for i,bound_variable in enumerate(bound_variables_left):
                        type_match = re.search(":(.*)", bound_variable)
                        if type_match != None:
                            bound_variables_left[i] = bound_variable.replace(type_match.group(0),"")

                    #More than one bound variable - check whether they match the current bound variable
                    
                    to_substitute_comparison = to_substitute
                    if ":" in to_substitute:
                        head, sep, tail = to_substitute.partition(':')
                        to_substitute_comparison = head
                    if to_substitute_comparison in bound_variables_left:
                        #Bound variable repeated, need to check for the next instance of it and stop evaluating there
                        for i,letter in enumerate(function):
                            if letter == '%':
                                subst_container_match = re.search("%(.*?)\.", function[i:])
                                bound_value = subst_container_match.group(1)
                                type_match = re.search(":(.*)", bound_variable)
                                if type_match is not None:
                                    bound_value = bound_value.replace(type_match.group(0),"")
                                if to_substitute_comparison == bound_value:
                                    break
                        end_value = i
                        function = calculate_alpha(to_substitute, function, incoming, 0, end_value)
                        self.session_object.add_beta_step("Alpha converting, function is now "+str(function))
                    #If there is not more than one of the same bound variable detected, just alpha convert as normal
                    else:
                        function = calculate_alpha(to_substitute, function, incoming)
                        self.session_object.add_beta_step("Alpha converting, function is now "+str(function))
                #If there are no bound variables inside the string found, alpha convert as normal
                else:
                    function = calculate_alpha(to_substitute, function, incoming)
                    self.session_object.add_beta_step("Alpha converting, function is now "+str(function))

                #Replace the bound variable with the new incoming value up until the end point (the point where there's bound variable crossover)
                new_function = function[:end_value].replace(to_substitute,incoming) + function[end_value:]
                self.session_object.add_beta_step("Replacing "+str(to_substitute)+ " with "+str(incoming)+" to get "+str(new_function))

            #If there are no other lambda terms found within the current lambda term
            else:
                #Calculate the alpha reduction as normal
                new_function = calculate_alpha(to_substitute, function, incoming)
                self.session_object.add_beta_step("Alpha converting, function is now "+str(function))
                #Replace the bound variable with the new incoming value
                new_function = new_function.replace(to_substitute,incoming)
                self.session_object.add_beta_step("Replacing "+str(to_substitute)+ " with "+str(incoming)+" to get "+str(new_function))

            #Check valid/invalid type by comparing the incoming type to the bound variable type
            if to_substitute_type is not None:
                to_substitute_type_journey = to_substitute_type.split("->")
                if incoming_type is not None:
                    incoming_type_journey = incoming_type.split("->")
                    if to_substitute_type_journey[0] != incoming_type_journey[0]:
                        #self.valid_typing = False
                        self.set_valid_typing(False)

            #Create a tree of the result of the inner function, and evaluate it
            tree = self.create_tree(new_function)
            if tree == -2 or tree == -1:
                return tree
            new_function,function_type,valid_typing = self.visit(tree)

            if valid_typing == False:
                self.set_valid_typing(False)

        #If there is not a value to substitute into this abstraction
        else:
            tree = self.create_tree(new_function)
            new_function,function_type,valid_typing = self.visit(tree)

            if valid_typing == False:
                self.set_valid_typing(False)

            #If there's nothing to do here, just convert back to %x.M form
            #and pass the value back up the tree, adding the types back in
            if to_substitute_type is not None:
                #if to_substitute doesn't already have a type
                if ":" not in to_substitute:
                    substitution_form = "%"+str(to_substitute)+":"+str(to_substitute_type)+"."
                else:
                    substitution_form = "%"+str(to_substitute) + "."
            else:
                substitution_form = "%"+str(to_substitute)+"."

            new_function = substitution_form + new_function
        
        #Create the new abstraction type, which is the bound variable type -> the type it gets converted to
        abstraction_type = str(to_substitute_type) + "->" + str(function_type)
        
        return new_function, abstraction_type

    def add_variable_to_context(self,variable,variable_type):
        if variable_type is not None and variable_type != "None":

            variable_list = []
            typing_list = []
            for context in self.current_typing_context:
                variable_list.append(context.get_variable())
                typing_list.append(context.get_variable_type())

            variable_type = variable_type.lower()
            if variable in variable_list:
                type_index = variable_list.index(variable)
                type_clash = typing_list[type_index].lower()

                if type_clash != variable_type:
                    self.set_valid_typing(False)

                    #If a variable clash has been found, remove it from the typing context
                    self.current_typing_context.pop(type_index)
            else:
                new_typing_context = self.TypingContextObject(variable, variable_type)
                self.current_typing_context.append(new_typing_context)
            
    def send_current_to_super_context(self):

        for current_context in self.current_typing_context:
            self.super_typing_context.append(current_context)
        
        self.current_typing_context.clear()
    
    def set_valid_typing(self,result):
        if self.valid_typing == True:
            self.valid_typing = result

    def post_process_contexts(self):
        self.super_typing_context = list(dict.fromkeys(self.super_typing_context))

        for context in self.super_typing_context:
            variable = context.get_variable()
            variable = variable.replace("*","")
            context.set_variable(variable)
        
    def update_typing_contexts(self, bound_variable):
        variable_contexts = []
        for context in self.current_typing_context:
            variable_contexts.append(context.get_variable())

        context_log = bound_variable
        #while context_log in self.current_typing_context:
        while context_log in variable_contexts:
            context_log = context_log + "*"

        #if bound_variable in self.current_typing_context:
        if bound_variable in variable_contexts:
            index = variable_contexts.index(bound_variable)
            self.current_typing_context[index].set_variable(context_log)

    class TypingContextObject():
        def __init__(self, variable, variable_type):
            self.variable = variable
            self.variable_type = variable_type
        
        def __repr__(self):
            return "[" + self.variable + "," + self.variable_type + "]"
    
        def __hash__(self):
            return hash(str(self))

        def __eq__(self, other):
            return str(self) == str(other)
    
        def get_variable(self):
            return self.variable
        
        def get_variable_type(self):
            return self.variable_type

        def set_variable(self,value):
            self.variable = value
            
    def send_context_to_session(self):
        write_string = ""
        for context in self.super_typing_context:
            write_string = write_string + "" + context.get_variable() + ": " + context.get_variable_type() + "&ensp;&ensp;&ensp;"
        
        self.session_object.set_typing_context(write_string)