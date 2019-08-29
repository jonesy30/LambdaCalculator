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

#Class which acts as the base class for the beta-reduction visitors, sharing all common code

class BaseVisitor(LambdaCalculusVisitor):

    def __init__(self):
        super()
        self.final_result = ""

    #On object deletion, save the final result to the session object (used to keep track of information between webpages)
    def __del__(self):
        self.session_object.add_beta_step("Final result = "+str(self.final_result))
    
    # Visit a parse tree produced by LambdaCalculusParser#term.
    def visitTerm(self, ctx:LambdaCalculusParser.TermContext):
        
        #depth == 1 is when the program hits the topmost node, post process when this happens
        depth = ctx.depth()
        if depth == 1:
            
            output = None
            return_type = None

            #Get the output tuple (result, return type and type validity)
            output_tuple = self.visitChildren(ctx)
            if output_tuple == -1:
                return -1
            elif output_tuple is not None:
                output = output_tuple[0]
                return_type = output_tuple[1]

            #Store the type context of the current scope in the main typing context for the entire term
            self.send_current_to_super_context()

            #Remove all *'s from the variables in the current context (used to distinguish different objects with similar names)
            #and save it to the session object for the program (used for sharing information between webpages)
            self.post_process_contexts()
            self.send_context_to_session()

            #Return the output, the return type and the type validity
            self.final_result = output
            return output,return_type,self.valid_typing

        else:
            #If I am not a topmost node, just visit my children as normal
            return self.visitChildren(ctx)

    # Visit a parse tree produced by LambdaCalculusParser#function.
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext):

        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am with "( [my_inner_term] )"
        if parenthesis_check == "(":
            child_value,child_type,input_type = self.visit(ctx.getChild(1))
            return "" + ctx.getChild(0).getText() + child_value + ctx.getChild(2).getText(),child_type,input_type
        
        #Get the result of the leftmost value
        returned_left = self.visit(ctx.getChild(0))

        #Get the value and the type from the returned left value
        left = returned_left[0]
        left_type = returned_left[1]

        #Get the result of the rightmost value
        returned_right = self.visit(ctx.getChild(2))
        
        #Get the value and type from the returned right value
        right = returned_right[0]
        right_type = returned_right[1]

        #Get the inner operation
        op = ctx.getChild(1).getText()

        #Convert types to lowercase to prevent type clashes as a result of uppercase/lowercase not being recognised as the same letter
        if left_type is not None:
            left_type = left_type.lower()
        
        if right_type is not None:
            right_type = right_type.lower()

        #Operation lists to determine the input/output type of the function
        #Functions that take two booleans and return a boolean
        bool_bool = ["&","|"]
        #Take two ints and return an int
        int_int = ["+","-","*","/","^"]
        #Takes two ints and returns a boolean
        int_bool = ["==",">","<"]

        #Initialise the return and input type which will be set later
        return_type = None
        input_type = None

        #If the middle operation converts a boolean to a boolean
        if op in bool_bool:
            #If either the left or right term is integer, the typing is invalid
            if left_type == "int" or right_type == "int":
                self.set_valid_typing(False)
            elif self.valid_typing == True:
                #If the term has valid typing, the input to and output from this function are both boolean values
                return_type = "bool"
                input_type = "bool"
        #If the middle operation converts an integer to an integer
        elif op in int_int:
            #If either the left or right term is a boolean, the typing is invalid
            if left_type == "bool" or right_type == "bool":
                self.set_valid_typing(False)
            elif self.valid_typing == True:
                #If the term has valid typing, the input to and output from this function are both integers
                return_type = "int"
                input_type="int"
        #If the middle operation converts an integer to a boolean
        elif op in int_bool:
            #If either the left or right term is a boolean, the typing is invalid
            if left_type == "bool" or right_type == "bool":
                self.set_valid_typing(False)
            elif self.valid_typing == True:
                #If the term has valid typing, the input to the function is an integer and the output is a boolean
                return_type = "bool"
                input_type = "int"

        #If the input type is a function we can't work out what the input type is
        if isinstance(ctx.getChild(0),LambdaCalculusParser.FunctionContext) or isinstance(ctx.getChild(2),LambdaCalculusParser.FunctionContext):
            input_type = None

        #Create the final string to be returned by the function
        return_string = "" + left + op + right

        #If left and right are letters which aren't TRUE or FALSE, it is a variable which needs to be saved to the typing context
        if left.isalpha() and len(left)<2:
            #Save the left variable and type to the typing context if it is a variable
            self.add_variable_to_context(left,input_type)
        if right.isalpha() and len(right)<2:
            #Save the right variable and type to the typing context if it is a variable
            self.add_variable_to_context(right,input_type)
        
        return return_string,return_type,input_type
    
    # Visit a parse tree produced by LambdaCalculusParser#variable.
    def visitVariable(self, ctx:LambdaCalculusParser.VariableContext):
        variable = (ctx.getChild(0)).getText()

        #If the variable has no third node (no type)
        if ctx.getChild(2) is None:
            #Just return as I am with no typing
            return ctx.getText(),None
        else:
            #If the variable does have a type, save this type to the typing context
            variable_type = self.visit(ctx.getChild(2))
            self.add_variable_to_context(variable, variable_type)

            #Return the variable and the type
            return ctx.getText(),variable_type

    # Visit a parse tree produced by LambdaCalculusParser#abstraction_term.
    def visitAbstraction_term(self, ctx:LambdaCalculusParser.Abstraction_termContext):
        #The abstraction is in form %[bound_variable]. , just return the bound variable up the tree
        return self.visit(ctx.getChild(1))
        
    # Visit a parse tree produced by LambdaCalculusParser#number.
    def visitNumber(self, ctx:LambdaCalculusParser.NumberContext):
        #Numbers have type int, return the number and type int
        return ctx.getChild(0).getText(),"int"

    # Visit a parse tree produced by LambdaCalculusParser#boolean_value.
    def visitBoolean_value(self, ctx:LambdaCalculusParser.Boolean_valueContext):
        #Boolean values have type bool, return the boolean value and type bool
        return ctx.getChild(0).getText(),"bool"
    
    # Visit a parse tree produced by LambdaCalculusParser#operation.
    def visitOperation(self, ctx:LambdaCalculusParser.OperationContext):
        #This is the operation in the middle of a function (e.g. + in 3+1)
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by LambdaCalculusParser#expression.
    def visitValue(self, ctx:LambdaCalculusParser.ValueContext):
        #A value can be a number, a variable or a boolean value, just check for parentheses and return as I am
        parenthesis_check = self.check_for_parenthesis(ctx)
        if parenthesis_check != -1:
            return parenthesis_check
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by LambdaCalculusParser#term_type.
    def visitFunction_type(self, ctx:LambdaCalculusParser.Function_typeContext):
        #A function type is just a type (the name "type" couldn't be used because this is a keyword in python)
        #Just return the type exactly as I am
        return ctx.getText()

    #A function which type-checks the application by comparing the redex type (function type) with the incoming type
    def type_check_application(self, function_type, expression_type):
        #Array which will store the final application type
        application_type_journey = []

        if function_type is not None:
            #Split the type of the function term into their ground types (1 -> 2 -> 3 -> ...n)
            function_type_journey = function_type.split("->")
            if expression_type is not None:
                #Do the same splitting with the type of the expression
                expression_type_journey = expression_type.split("->")

                #Check whether the typing is valid or not
                if len(function_type_journey) > len(expression_type_journey):
                    #Variable which will be used to flag if the ground types at any point don't match
                    type_mismatch = False
                    #While the right hand term still has ground types left to process
                    while len(expression_type_journey) > 0:
                        #If the ground types don't match
                        if function_type_journey[0] != expression_type_journey[0]:
                            #Convert both types to lowercase to prevent accidental mismatch through case
                            function_journey_step = function_type_journey[0].lower()
                            expression_journey_step = expression_type_journey[0].lower()
                            #If either ground type is none, the type is still valid even if they're not the same
                            if function_journey_step == "none" or expression_journey_step == "none":
                                #Remove the first ground type of both journeys and continue
                                del function_type_journey[0]
                                del expression_type_journey[0]
                            else:
                                #If they are not the same and one of them is not none, there is a type mismatch
                                expression_type_journey = []
                                type_mismatch = True
                        else:
                            #Remove the first ground type of both journeys and continue
                            del function_type_journey[0]
                            del expression_type_journey[0]
                    if type_mismatch == False:
                        application_type_journey = function_type_journey
                    else:
                        self.set_valid_typing(False)
            else:
                #Set the application type to the bit of the function type which is leftover
                del function_type_journey[0]
                application_type_journey = function_type_journey
    
        #Set the application type journye to None if needed
        if application_type_journey == [] or application_type_journey == None:
            application_type = "None"
        else:
            #Create the abstraction type string based on what's left of the function type term
            application_type = ""
            for i,journey_step in enumerate(application_type_journey):
                application_type = application_type + "->" + application_type_journey[i]
            application_type=application_type[2:]
    
        return application_type

    #Function which takes the type of the bound variable and adds it into all variables it refers to in the rest of the term
    def add_bound_variable_types_to_function(self, bound_variable, function, type):
        
        #If the bound variable has a type in the string, remove it and ignore it (since we already have
        #the type incoming to the function)
        if ":" in bound_variable:
            head, sep, tail = bound_variable.partition(':')
            bound_variable = head

        #If there is a type to set the rest of the values to
        if type is not None:
            #Convert the string to a list so it can be accessible by index
            function_list = list(function)
            #Add a blank space to the end of the list to prevent overflow when checking if a : exists after a variable
            function_list.append(" ")
            #For each character in the function
            for i,character in enumerate(function_list):
                #If the character is a bound variable and it doesn't already have a type, add the bound variable type to that character
                if character == bound_variable:
                    if function_list[i+1] != ":":
                        function_list[i] = character + ":" + type

            #Convert the final list back into a string and return
            processed_function = "".join(function_list)
            
            return processed_function
        else:
            return function

    #Function which turns the string "none" into the Python struct None
    def convert_type_if_none(self, term_type):
        
        #If the type is a string
        if term_type is not None:
            #Convert the type to lowercase to prevent unrecognition due to uppercase letters
            term_type = term_type.lower()
            #Set the type to None if it is of the string "none"
            if term_type == "none":
                term_type = None
            
        return term_type

    #Function which creates an abstract-syntax-tree from a subterm of the term (used to process abstractions)
    def create_tree(self, function):
        #If there is a term to create a tree from
        if function is not None:
            #Pass it through the ANTLR generated classes as required
            stream = InputStream(function)
            lexer = LambdaCalculusLexer(stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(LambdaErrorListener())
            tokens = CommonTokenStream(lexer)
            parser = LambdaCalculusParser(tokens)
            tree = parser.term()

            #Return the resultant abstract syntax tree
            return tree

    #Function which checks for parenthesis () and returns the processed section inside the brackets if so
    def check_for_parenthesis(self, ctx):
        parenthesis_check = ctx.getChild(0).getText()
        #If the left child is (, there are parentheses
        if parenthesis_check == "(":
            #So visit the middle child and return the string representation of the result (including the brackets)
            child_value,child_type = self.visit(ctx.getChild(1))
            return "" + ctx.getChild(0).getText() + str(child_value) + ctx.getChild(2).getText(),child_type
        #Return -1 if there are no brackets found
        else:
            return -1
    
    #Function which performs the part of the abstraction functionality which is shared by all beta-visitors
    def perform_abstraction(self, ctx, incoming, incoming_type, to_substitute, to_substitute_type):

        #If the types of the substituted or incoming values are the string "none" (or any capitalised version of none)
        #set it to standard value None (makes type checking and setting easier later)
        incoming_type = self.convert_type_if_none(incoming_type)
        to_substitute_type = self.convert_type_if_none(to_substitute_type)

        #Visit and evaluate the right hand side child (the function), get the function and the function type from the result
        returned_child = self.visit(ctx.getChild(2))

        function = returned_child[0]
        function_type = returned_child[1]

        comparison_child = self.remove_types(ctx.getChild(2).getText())
        comparison_function = self.remove_types(function)

        if comparison_child!=comparison_function:
            self.session_object.add_beta_step("Using the lambda-reduction rule to get to "+str(comparison_function))

        #The right hand child could be a function, if so it will contain an "input_type" variable from type inference
        #If there are more variables to unpack, get the inferred input type
        input_type = None
        if len(returned_child) == 3:
            input_type = returned_child[2]
        
        #If no typing information about the bound variable has been found, set it to the incoming type (so it can be checked for type validity)
        if to_substitute_type == None:
            to_substitute_type = input_type

        #Add the new bound variable type to all associated variables in the rest of the function
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
                        before_alpha = function
                        function = calculate_alpha(to_substitute, function, incoming, 0, end_value)

                        if before_alpha != function:
                            substitution_form = "%"+str(to_substitute)+"."
                            printed_form = substitution_form + str(function)
                            self.session_object.add_beta_step("Alpha converting, abstraction is now "+str(printed_form))
                    #If there is not more than one of the same bound variable detected, just alpha convert as normal
                    else:
                        before_alpha = function
                        function = calculate_alpha(to_substitute, function, incoming)

                        if before_alpha != function:
                            substitution_form = "%"+str(to_substitute)+"."
                            printed_form = substitution_form + str(function)
                            self.session_object.add_beta_step("Alpha converting, abstraction is now "+str(printed_form))
                #If there are no bound variables inside the string found, alpha convert as normal
                else:
                    before_alpha = function
                    function = calculate_alpha(to_substitute, function, incoming)

                    if before_alpha != function:
                        substitution_form = "%"+str(to_substitute)+"."
                        printed_form = substitution_form + str(function)
                        self.session_object.add_beta_step("Alpha converting, abstraction is now "+str(printed_form))

                #Replace the bound variable with the new incoming value up until the end point (the point where there's bound variable crossover)
                new_function = function[:end_value].replace(to_substitute,incoming) + function[end_value:]
                self.session_object.add_beta_step("Using the beta rule, replacing "+str(to_substitute)+ " with "+str(incoming)+" to get "+str(new_function))

            #If there are no other lambda terms found within the current lambda term
            else:
                #Calculate the alpha reduction as normal
                before_alpha = function
                new_function = calculate_alpha(to_substitute, function, incoming)

                if before_alpha != new_function:
                    substitution_form = "%"+str(to_substitute)+"."
                    printed_form = substitution_form + str(new_function)
                    self.session_object.add_beta_step("Alpha converting, abstraction is now "+str(printed_form))
                #Replace the bound variable with the new incoming value
                new_function = new_function.replace(to_substitute,incoming)
                self.session_object.add_beta_step("Using the beta rule, replacing "+str(to_substitute)+ " with "+str(incoming)+" to get "+str(new_function))

            #Check valid/invalid type by comparing the incoming type to the bound variable type
            if to_substitute_type is not None:
                #Split the subsitutition type into its individual ground types
                to_substitute_type_journey = to_substitute_type.split("->")
                if incoming_type is not None:
                    #Split the incoming type into its individual ground types
                    incoming_type_journey = incoming_type.split("->")
                    #If the to_subsitute type and the incoming type are not equal, typing is invalid
                    if to_substitute_type_journey[0] != incoming_type_journey[0]:
                        self.set_valid_typing(False)

            #Create a tree of the result of the inner function, and evaluate it
            tree = self.create_tree(new_function)
            if tree == -2 or tree == -1:
                return tree
            new_function,function_type,valid_typing = self.visit(tree)

            #Process the type validity of the inner tree (if it is invalid, then this parent term is invalid)
            if valid_typing == False:
                self.set_valid_typing(False)

        #If there is not a value to substitute into this abstraction
        else:
            #Create a tree of the inner function and evaluate it
            tree = self.create_tree(new_function)
            new_function,function_type,valid_typing = self.visit(tree)

            #Process the type validity of the inner tree (if it is invalid, then this parent term is invalid)
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

    #Method which adds a variable with an associated type to the typing context for the current scope
    def add_variable_to_context(self,variable,variable_type):

        #If the variable has a type (is INT or BOOL - None's are not saved)
        if variable_type is not None and variable_type != "None":

            variable_list = []
            typing_list = []

            #Check the incoming variable against the variables in the current typing context to check for any type clashes
            #Store each variable and their associated type in two lists so they can be compared
            for context in self.current_typing_context:
                variable_list.append(context.get_variable())
                typing_list.append(context.get_variable_type())

            #Set the variable type to lowercase (to prevent "Int" being recognised as different to "int")
            variable_type = variable_type.lower()

            #If the incoming variable already has a type in the current typing context
            if variable in variable_list:

                #Check the existing type of that variable
                type_index = variable_list.index(variable)
                type_clash = typing_list[type_index].lower()

                #If the existing type does not match the incoming type, there is a type clash and the type validity is FALSE
                if type_clash != variable_type:
                    self.set_valid_typing(False)

                    #If a variable clash has been found, remove it from the typing context since it is invalid
                    self.current_typing_context.pop(type_index)
            else:
                #If is is not found in the current typing context, create a new TypingContextObject which stores the variable name and type
                #and append it to the current typing context
                new_typing_context = self.TypingContextObject(variable, variable_type)
                self.current_typing_context.append(new_typing_context)
            
    #Method which holds the current typing context (used to separate the types within different scopes)
    #and save it to the super context (the main context covering the entire term)
    def send_current_to_super_context(self):

        #For each variable-type pair in the current context, add it to the super context
        for current_context in self.current_typing_context:
            self.super_typing_context.append(current_context)
        
        #Reset the current context ready for a new scope
        self.current_typing_context.clear()
    
    #Setter protection which only allows the return type of the final term to be set if the
    #typing context is valid
    def set_valid_typing(self,result):
        if self.valid_typing == True:
            self.valid_typing = result

    #Method which removes all *'s in each variable within the typing context
    #(*'s are used to distinguish different objects with the same variable name in a scope)
    def post_process_contexts(self):
        #Remove all duplicates from the super typing context
        self.super_typing_context = list(dict.fromkeys(self.super_typing_context))

        #For each context, remove all *'s from the associated variable
        for context in self.super_typing_context:
            variable = context.get_variable()
            variable = variable.replace("*","")
            context.set_variable(variable)
        
    #Method which adds a * to all bound variables within the term
    #(used to allow like-variables to have different types when they refer to different objects)
    def update_typing_contexts(self, bound_variable):
        variable_contexts = []

        #For each context in the current typing context
        for context in self.current_typing_context:
            variable_contexts.append(context.get_variable())

        #Add a * at the end of the bound variable
        context_log = bound_variable
        while context_log in variable_contexts:
            context_log = context_log + "*"

        if bound_variable in variable_contexts:
            index = variable_contexts.index(bound_variable)
            self.current_typing_context[index].set_variable(context_log)

    #Class used to store variable-type pairs for the typing context of the term
    class TypingContextObject():

        #each typing context object has a variable with an associated type
        def __init__(self, variable, variable_type):
            self.variable = variable
            self.variable_type = variable_type
        
        #If the typing context is printed, print in [variable,type] form
        def __repr__(self):
            return "[" + self.variable + "," + self.variable_type + "]"
    
        #Used to remove duplicates via storing a list of typing contexts in a dictionary
        def __hash__(self):
            return hash(str(self))

        #Also used to remove duplicates via storing a list of typing contexts in a dictionary
        def __eq__(self, other):
            return str(self) == str(other)
    
        #Get the variable part of the typing context
        def get_variable(self):
            return self.variable
        
        #Get the type part of the typing context
        def get_variable_type(self):
            return self.variable_type

        #Change the variable name (used when *'s are being added to the string for
        #terms which have the same variable name but refer to different objects - and therefore
        #could have multiple terms)
        def set_variable(self,value):
            self.variable = value
            
    #Writes the typing context for the entire term in String form to the session object (used for sharing information between webpages)
    def send_context_to_session(self):
        write_string = ""
        for context in self.super_typing_context:
            write_string = write_string + "" + context.get_variable() + ": " + context.get_variable_type() + "&ensp;&ensp;&ensp;"
        
        #Set the session object to the string representation of the typing context
        self.session_object.set_typing_context(write_string)

    #Function which removes all types from the output term (since this is covered by the typing context and the final type)
    def remove_types(self, output):
        bad_strings = [":int",":Int",":INT",":bool",":Bool",":BOOL",":None",":NONE",":none"]

        #Replace all types with no character (deleting them)
        output = str(output)
        for string in bad_strings:
            output = output.replace(string,"")
        
        return output