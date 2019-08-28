from BracketCheck import BracketCheck
from Stack import Stack
import sys
import re

#Python file which takes an incoming lambda term as one string and alpha-converts it as a whole
#This is done by determining the scope of each bound variable in the expression and building a scope-map, which is used
#to check if there could be a variable clash

#Class used to help identify the individual scopes of bound variables within a lambda term
class ScopeObject(object):
    def __init__(self, id, parent):
        self.id = id
        self.parent = parent
        self.start_index = None
        self.end_index = None
        self.brackets = Stack()

    def getParent(self):
        return self.parent

    def setStartIndex(self, index):
        self.start_index = index

    def setEndIndex(self,index):
        self.end_index = index
    
    def __repr__(self):
        return "id = "+str(self.id)+", start = "+str(self.start_index)+", end = "+str(self.end_index)

#Class which performs the alpha conversion and returns the result
class AlphaCalculatorFromComplete():
    def __init__(self):
        available_letters = []

    #Look for the letter after the lambda (%) operator to find the variables bound in the current scope
    def get_bound_values(self, data):
        bound_values = []
        if data is not None:
            abstraction_list = list(data)
            for i, letter in enumerate(abstraction_list[:-1]):
                if letter == '%':
                    bound_values.append(abstraction_list[i+1])
        
        return bound_values

    #Method to make sure the brackets are all matched up in the string the user has entered
    def check_brackets(self, expression):
        bracket_checker = BracketCheck()

        matched_brackets = bracket_checker.check_brackets(expression)

        while matched_brackets == False:
            expression = input("Sorry, mismatched brackets, check and try again?")
            matched_brackets = bracket_checker.check_brackets(expression)
        
        return expression

    #Method to create a map of each letter according to their scopes (identifiable with ids), and a list of scopes those ids represent
    def get_scopes(self, expression):
        scope_objects = []
        scope_id = 0

        #Initialise the first scope and get the starting point using the % symbol
        current_scope = ScopeObject(scope_id,None)
        if expression[0] != '%':
            current_scope.setStartIndex(0)
            scope_objects.append(current_scope)
        
        #For each letter in the expression
        for i,letter in enumerate(expression):
            #If you've come across a %, you've hit a new scope. Incremement the scope id and start counting fresh
            if letter == '%':
                scope_id = scope_id + 1
                current_scope = ScopeObject(scope_id,current_scope)
                current_scope.setStartIndex(i)
                scope_objects.append(current_scope)
            #Use brackets to help determine the current scope
            elif letter == '(':
                current_scope.brackets.push(letter)
            #If a close bracket is found, that might mean the end of a scope, check if there's a matching open bracket within this scope
            #If not - you've got a new scope
            elif letter == ')':
                while current_scope.brackets.is_empty():
                    current_scope.setEndIndex(i)
                    current_scope = current_scope.getParent()
                current_scope.brackets.pop()

        #If any scopes haven't had their end_index set (the point where the scope ends), the scope ends at the end of the string
        #So set the scope as the end of the string
        for scope in scope_objects:
            if scope.end_index is None:
                scope.end_index = len(expression)

        #Create a string which is the length of the expression and represent each index by what it belongs to
        #For example (%x.x+1)3 could become 001111102 for each of the scope ids
        scope_map = [0] * len(expression)

        for scope in scope_objects:
            i = scope.start_index
            while i < scope.end_index:
                scope_map[i] = scope.id
                i = i + 1

        #Return a list of the scope map and the objects each index corresponds to
        return scope_map, scope_objects

    #Get the letters which do not appear in the expression and therefore which can be used as replacement values
    def get_available_letters(self, expression,incoming):
        #Note to self: I'm allowing capitals!
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        available_letters = list(alphabet)

        #Remove all letters found in the expression from the list of available letters
        for letter in expression:
            if letter in available_letters:
                available_letters.remove(letter)
        
        #Remove all the letters found in the incoming term from the list of available letters
        if incoming is not None and incoming != "None":
            for letter in incoming:
                if letter in available_letters:
                    available_letters.remove(letter)

        self.available_letters = available_letters

    #Work out what the bound variables are to be renamed to from the list of available non-clashing letters
    def rename_bound_values(self, expression):
        
        expression_list = list(expression)
        #Get the list of the letters which are to be replaced
        to_replace = self.get_bound_values(expression)

        #Create a dictionary of all the values to replace and what they should be replaced with
        replace_with = [""] * len(to_replace)
        #For each letter to replace
        for i,value_to_replace in enumerate(to_replace):
            #Create a new array to make sure conflicting bound variables aren't being registered as the same object
            #for example in (%x.%x.x+1) -- the first and second x's are different objects so treat them as such
            other_bound_values = to_replace.copy()
            other_bound_values.remove(value_to_replace)
            if value_to_replace in other_bound_values:
                #If there are values left over which are to be replaced
                replace_with[i] = self.available_letters[0]
                self.available_letters.remove(replace_with[i])
            else:
                replace_with[i] = value_to_replace 
            
        #Return the list of variables to be replaced and what they are to be replaced with
        return to_replace,replace_with

    #A function which works out what the free variables are to be renamed to if appropriate in the same way as the bound variables above
    def rename_free_values(self, expression, scope_objects):

        #Get the list of free variables that are to be replaced
        expression_list = list(expression)
        to_replace = self.free_variables(scope_objects,expression)
        to_replace = list(dict.fromkeys(to_replace))

        #Remove duplicates in free variables, just incase there are any still left
        replace_with = [""] * len(to_replace)
        for i,value_to_replace in enumerate(to_replace):
            replace_with[i] = self.available_letters[0]
            self.available_letters.remove(replace_with[i])

        #Return the list of variables to be replaced and waht they are to be replaced with
        return to_replace,replace_with

    #A function which renames all potentially clashing values in the original expression to available letters
    def rename_values(self, expression, scope_objects, free_variables=False):
        
        #Create a list out of the expression (so indexes can be replaced)
        expression_list = list(expression)

        #For each scope
        for scope in scope_objects:

            term = ""
            i = scope.start_index
            while i < scope.end_index:
                term = term + expression[i]
                i = i + 1

            #If the function is set to rename the free variables (as opposed to the bound variables)
            if free_variables == True:
                #Get the variables to replace the free variable with
                to_replace, replace_with = self.rename_free_values(expression, scope_objects)
            #Else teh bound variables are to be renamed
            else:
                #Get the bound values and what they are to be replaced with
                to_replace, replace_with = self.rename_bound_values(expression)

            #Replace each relevant variable in the string
            i = scope.start_index
            while i < scope.end_index:
                if expression[i] in to_replace:
                    expression_list[i] = replace_with[to_replace.index(expression[i])]
                i = i + 1
            
            #Create a string from the list created
            expression = "".join(expression_list)

        #Return the alpha-converted string
        return expression

    #This is for testing alone - it just prints a list of scopes and their start and end indexes
    def test_print(self, scope_objects,expression):

        expression_list = list(expression)
        for scope in scope_objects:
            print()
            print(scope.id)
            
            scope_string = ""
            i = scope.start_index
            while i < scope.end_index:
                scope_string = scope_string + expression_list[i]
                i = i + 1
            
            print(scope_string)

    #Find the free variables in the term and save them to the list of free variables in the object
    def get_free_variables(self, scope_objects_expression, scope_objects_incoming, expression, incoming):

        free_variables = []
        free_variables_expression = self.free_variables(scope_objects_expression, expression)
        for variable in free_variables_expression:
            free_variables.append(variable)

        free_variables_incoming = self.free_variables(scope_objects_incoming, incoming)
        for variable in free_variables_incoming:
            if variable not in free_variables:
                free_variables.append(variable)

    #Get the list of free variables from the list of scope objects (and what bound variables they contain within them)
    def free_variables(self, scope_objects, term):
        
        free_variables = []
        term_list = list(term)
        
        #Look at the scope objects in reverse order (innermost first)
        for scope in scope_objects[::-1]:
        
            scope_string = ""
            i = scope.start_index
            while i < scope.end_index:
                scope_string = scope_string + term_list[i]
                i = i + 1
            
            #Get all variables in the string of the current scope
            free_variables_found = re.findall("[a-zA-Z]",scope_string)
            #Remove duplicate letters
            free_variables_found = list(dict.fromkeys(free_variables_found))

            #Find the bound variables within the current scope using regex
            bound_variable_container = re.search("%(.*?)\.", term)
            if bound_variable_container is not None:
                bound_variable = bound_variable_container.group(1)
                if bound_variable in free_variables_found:
                    free_variables_found.remove(bound_variable)

            for variable in free_variables_found:
                free_variables.append(variable)

        #Remove all duplicates in the free variables list
        free_variables = list(dict.fromkeys(free_variables))
        #Return the free variables
        return free_variables

    #Main method which performs the alpha conversion using the above methods
    def calculate_alpha(self, expression, incoming):

        if incoming is None or incoming == "None":
            #If there's nothing incoming, just alpha convert as normal
            #Get the list of scope objects
            scope_map, scope_objects = self.get_scopes(expression)
            #Get the list of the available letters based on the letters within the term
            self.get_available_letters(expression, None)
            #Rename the variables in accordance with alpha conversion
            expression = self.rename_values(expression, scope_objects,False)
        #If there is an incoming term
        else:
            #Get the list of scopes in the incoming and the expression
            scope_map_expression, scope_objects_expression = self.get_scopes(expression)
            scope_map_incoming, scope_objects_incoming = self.get_scopes(incoming)

            #Get the list of free variables in the term
            self.get_free_variables(scope_objects_expression,scope_objects_incoming, expression, incoming)  
            self.get_available_letters(expression, incoming)

            #Rename the expression free variables and bound variables in accordance with alpha conversion
            expression = self.rename_values(expression, scope_objects_expression,True)
            expression = self.rename_values(expression, scope_objects_expression,False)

        #Return the converted expression
        return expression

#main method - called when AlphaCalculatorFromComplete.py is called explicitly from the command line
if __name__ == "__main__":   

    alpha_calculator = AlphaCalculatorFromComplete()

    #Get the input and whether or not the brackets are valid (this is checked before the class is called when coming from the web interface or via LambdaCalculus.py)
    expression = input("Enter test expression: ")
    expression = alpha_calculator.check_brackets(expression)
    incoming = input("Enter incoming expression: ")
    incoming = alpha_calculator.check_brackets(incoming)

    #Calculate the alpha conversion and print the result
    expression = alpha_calculator.calculate_alpha(expression, incoming)
    print(expression)

#this continually overrides replaced variables in smaller scopes, which means some letters aren't used when they should be
#this might become an issue in the future when I start looking at larger lambda terms, but for now... It works? So leave it?





