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

class CallByValueVisitor(LambdaCalculusVisitor):

    def __init__(self):
        super()
        self.incoming_values = Stack() #NOTE: This definitely needs renamed
        self.valid_typing = True
    
    #NOTE: Order of functions is as follows:
    # visitTerm
    # visitApplication
    # visitAbstraction
    # visitFunction
    # visitVariable
    # visitAbstraction_term
    # visitNumber
    # visitOperation
    # visitValue
    # visitFunction_type
    
    # Visit a parse tree produced by LambdaCalculusParser#term.
    def visitTerm(self, ctx:LambdaCalculusParser.TermContext):
        print("T: "+ctx.getText())

        depth = ctx.depth()
        if depth == 1:
            
            #output,return_type = str(self.visitChildren(ctx))
            output,return_type = self.visitChildren(ctx)

            #NOTE: Format this so output returns a string and not an array            
            output,return_type = self.post_process(output, return_type)
            return output,return_type,self.valid_typing

        else:
            return self.visitChildren(ctx)

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

        application_type = None
        #If the left hand tree is an abstraction - you're not done! Keep processing using the right hand side of the tree
        if isinstance(am_I_an_abstraction,LambdaCalculusParser.AbstractionContext):
            #Visit the left hand tree with the term created from the right hand side
            self.incoming_values.push(tuple([expression,expression_type]))
            function,function_type = self.visit(am_I_an_abstraction)

            #Type check the application
            application_type_journey = []

            if function_type is not None:
                #Split the type of the function term into their journeys (1 -> 2 -> 3 -> ...n)
                print("Function type not none! "+function_type)
                function_type_journey = function_type.split("->")
                if expression_type is not None:
                    #Do the same splitting with the type of the expression
                    print("Expression type = "+expression_type)
                    expression_type_journey = expression_type.split("->")
                    application_type_journey = []

                    #Check whether the typing is valid or not
                    if len(function_type_journey) > len(expression_type_journey):
                        type_mismatch = False
                        while len(expression_type_journey) > 0:
                            if function_type_journey[0] != expression_type_journey[0]:
                                function_journey_step = function_type_journey[0].lower()
                                expression_journey_step = expression_type_journey[0].lower()
                                if function_journey_step != "none" and expression_journey_step != "none":
                                    expression_type_journey = []
                                    type_mismatch = True
                                else:
                                    #NOTE: Repeated code
                                    del function_type_journey[0]
                                    del expression_type_journey[0]
                            else:
                                del function_type_journey[0]
                                del expression_type_journey[0]
                        if type_mismatch == False:
                            application_type_journey = function_type_journey
                else:
                    print("In else")
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

            print("Application_type = "+str(application_type))
        #The left hand side isn't an abstraction, keep the left hand side as it is, and add the right
        else:
            function = function + expression

        #Return the application value and type
        print("Returned value in application = "+function)
        return function,application_type

    # Visit a parse tree produced by LambdaCalculusParser#abstraction.
    def visitAbstraction(self, ctx:LambdaCalculusParser.AbstractionContext):
        print("Abstraction = "+ctx.getText())

        parenthesis_check = ctx.getChild(0).getText()
        #if I am a parenthesis of myself, just return as I am
        if parenthesis_check == "(":
            child_value,child_type = self.visit(ctx.getChild(1))
            return "" + ctx.getChild(0).getText() + child_value + ctx.getChild(2).getText(),child_type
        
        #NOTE: These all definitely need renamed
        #Visit the left hand child, to get the bound variable type and value
        to_substitute,to_substitute_type = self.visit(ctx.getChild(0))

        #Pop the value as soon as you get the abstraction term, before you
        #visit the rest of the children, so the correct term gets associated
        #with the correct input
        incoming_tuple = self.incoming_values.pop()

        #Split the incoming tuple into its value and type terms
        incoming = None
        incoming_type = None
        
        if incoming_tuple == -1:
            incoming = incoming_tuple
        else:
            incoming = incoming_tuple[0]
            incoming_type = incoming_tuple[1]
        
        #If the types of the substituted or incoming values are the string "none" (or any capitalised version of none)
        #set it to standard value None (makes type checking and setting easier later)
        incoming_type = self.convert_type_if_none(incoming_type)
        to_substitute_type = self.convert_type_if_none(to_substitute_type)

        #Visit and evaluate the right hand side child (the function)
        function,function_type = self.visit(ctx.getChild(2))

        print("To substitute = "+to_substitute)
        print("Function before abstraction = "+function)
        print("Incoming before abstraction = "+str(incoming))

        new_function = function

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

                #NOTE: I could check that types match here?
                #Replace the bound variables with the incoming value, up until the end point (the point where there's bound variable crossover)
                print("New function at checkpoint marker 1 = "+new_function[:end_value])
                #Replace the bound variable with the new incoming value
                new_function = function[:end_value].replace(to_substitute,incoming) + function[end_value:]
                #Convert the new function to include the types from either the bound value or the incoming value (depending on which has a type)
                new_function = self.convert_function_with_type(to_substitute, to_substitute_type, incoming, incoming_type, new_function, end_value)

            #If there are no other lambda terms found within the current lambda term
            else:
                #Calculate the alpha reduction as normal
                new_function = calculate_alpha(to_substitute, function, incoming)
                #Replace the bound variable with the new incoming value
                new_function = new_function.replace(to_substitute,incoming)
                #Convert the new function to include the types from either the bound value or the incoming value (depending on which has a type)
                new_function = self.convert_function_with_type(to_substitute, to_substitute_type, incoming, incoming_type, new_function)

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
                        self.valid_typing = False

            print()
            print("New function before tree creation = "+str(new_function))
            print()

            #Create a tree of the result of the inner function, and evaluate it
            tree = self.create_tree(new_function)
            new_function,function_type,valid_typing = self.visit(tree)

            if valid_typing == False:
                self.valid_typing = False

            print()
            print("New function after tree creation = "+str(new_function))          
            print()  
        
        #If there is not a value to substitute into this abstraction
        else:
            #If there's nothing to do here, just convert back to %x.M form
            #and pass the value back up the tree, adding the types back in
            substitution_form = "%"+str(to_substitute)+":"+str(to_substitute_type)+"."
            new_function = substitution_form + function
        
        #Create the new abstraction type, which is the bound variable type -> the type it gets converted to
        abstraction_type = str(to_substitute_type) + "->" + str(function_type)
        print("Function after replacement in abstraction = "+new_function)
        print("Abstraction type = "+str(abstraction_type))
        #TODO: Implement proper typing here
        return new_function,abstraction_type

    # Visit a parse tree produced by LambdaCalculusParser#function.
    #NOTE: having function_type = None could be a way to fix my "invalid typing when bound variable does not match inner variable" issue
    #Just call this method directly from the abstraction term if the thing below is a function
    #NOTE: If I don't end up needing this, take it out!
    def visitFunction(self, ctx:LambdaCalculusParser.FunctionContext, function_type=None):
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

        #Functions that take two booleans and return a boolean
        bool_bool = ["AND","OR"]
        #Take two ints and return an int
        int_int = ["+","-","*","/","^"]
        #Takes two ints and returns a boolean
        int_bool = ["EQ","GT","LT"]
        return_type = None

        if op in bool_bool:
            if left_type == "int" or right_type == "int":
                self.valid_typing = False
            elif self.valid_typing == True:
                return_type = "bool"
        elif op in int_int or op in int_bool:
            if left_type == "bool" or right_type == "bool":
                self.valid_typing = False
            elif self.valid_typing == True:
                return_type = "int"
        
        #TODO: Do some actual calculations here
        return_string = "" + left + op + right
        
        return return_string,return_type
        #return "" + self.visit(ctx.getChild(0)) + ctx.getChild(1).getText() + self.visit(ctx.getChild(2))
    
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
    
    # Visit a parse tree produced by LambdaCalculusParser#term_type.
    def visitFunction_type(self, ctx:LambdaCalculusParser.Function_typeContext):
        return ctx.getText()

    #NOTE: Please rename this future Yola...
    def convert_function_with_type(self, to_substitute, to_substitute_type, incoming, incoming_type, function, end_value=None):

        #If there is a bound variable type to be substituted, add it to the rest of the bound variables in the term
        if to_substitute_type is not None:
            print(str(to_substitute_type))
            #incoming = incoming + ":" + incoming_type
            incoming = incoming + ":" + to_substitute_type

            function = function[:end_value].replace(to_substitute,incoming) + function[end_value:]
        
        #If the substituted type is none but the incoming type is not, we still know what the bound variable type should now be, so replace it
        elif incoming_type is not None:
            print("To substitute type is none, but incoming isn't!")
            incoming = incoming + ":" + incoming_type
            function = function[:end_value].replace(to_substitute,incoming) + function[end_value:]

        return function

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
        stream = InputStream(function)
        lexer = LambdaCalculusLexer(stream)
        tokens = CommonTokenStream(lexer)
        parser = LambdaCalculusParser(tokens)
        tree = parser.term()

        return tree