from BracketCheck import BracketCheck
from Stack import Stack
import sys
import re

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

    #Method to create a map of each letter according to their scope ids, and a list of scopes those ids represent
    def get_scopes(self, expression):
        scope_objects = []
        scope_id = 0

        current_scope = ScopeObject(scope_id,None)
        if expression[0] != '%':
            current_scope.setStartIndex(0)
            scope_objects.append(current_scope)
        
        for i,letter in enumerate(expression):
            if letter == '%':
                scope_id = scope_id + 1
                current_scope = ScopeObject(scope_id,current_scope)
                current_scope.setStartIndex(i)
                scope_objects.append(current_scope)
            elif letter == '(':
                current_scope.brackets.push(letter)
            elif letter == ')':
                while current_scope.brackets.is_empty():
                    current_scope.setEndIndex(i)
                    current_scope = current_scope.getParent()
                current_scope.brackets.pop()

        for scope in scope_objects:
            if scope.end_index is None:
                scope.end_index = len(expression)

        scope_map = [0] * len(expression)

        for scope in scope_objects:
            i = scope.start_index
            while i < scope.end_index:
                scope_map[i] = scope.id
                i = i + 1

        return scope_map, scope_objects

    def get_available_letters(self, expression,incoming):

        #Note to self: I'm allowing capitals!
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        available_letters = list(alphabet)

        for letter in expression:
            if letter in available_letters:
                available_letters.remove(letter)
        
        if incoming is not None and incoming != "None":
            for letter in incoming:
                if letter in available_letters:
                    available_letters.remove(letter)

        self.available_letters = available_letters

    def rename_values(self, expression,scope_objects):
        
        for scope in scope_objects:
            print("Scope = "+str(scope))
            term = ""
            i = scope.start_index
            while i < scope.end_index:
                term = term + expression[i]
                i = i + 1
        
            expression_list = list(expression)
            bound_values = self.get_bound_values(expression)
            print("Bound values = "+str(bound_values))

            replace_with = [""] * len(bound_values)
            for i,bound_value in enumerate(bound_values):
                other_bound_values = bound_values
                other_bound_values.remove(bound_value)
                if bound_value in other_bound_values:
                    print("Other bound values")
                    replace_with[i] = self.available_letters[0]
                    print("Replacing "+str(i)+" with "+replace_with[i])
                    self.available_letters.remove(replace_with[i])

                else:
                    replace_with[i] = bound_value

            i = scope.start_index
            while i < scope.end_index:
                if expression[i] in bound_values:
                    expression_list[i] = replace_with[bound_values.index(expression[i])]
                i = i + 1
            
            expression = "".join(expression_list)
            print("New expression = "+expression)

        return expression

    def rename_values_with_incoming(self, expression,scope_objects):
        
        for scope in scope_objects:
            print("Scope = "+str(scope))
            term = ""
            i = scope.start_index
            while i < scope.end_index:
                term = term + expression[i]
                i = i + 1
        
            expression_list = list(expression)
            free_variables = self.get_free_variables(scope_objects,expression)
            print("Free values = "+str(free_variables))

            to_replace = [""] * len(free_variables)
            replace_with = [""] * len(free_variables)

            #Remove duplicates in free variables, just incase there are any still left
            free_variables = list(dict.fromkeys(free_variables))
            for i,free_value in enumerate(free_variables):
                print("Processing free value "+str(free_value))
                to_replace[i] = free_value
                replace_with[i] = self.available_letters[0]
                self.available_letters.remove(replace_with[i])

            i = scope.start_index
            while i < scope.end_index:
                if expression[i] in free_variables:
                    expression_list[i] = replace_with[to_replace.index(expression[i])]
                i = i + 1
            
            expression = "".join(expression_list)
            print("New expression = "+expression)

        return expression


    #This is for testing alone
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

    def get_free_variables_with_incoming(self, scope_objects_expression, scope_objects_incoming, expression, incoming):

        free_variables = []
        free_variables_expression = self.get_free_variables(scope_objects_expression, expression)
        for variable in free_variables_expression:
            print("Variable expression = "+variable)
            free_variables.append(variable)

        free_variables_incoming = self.get_free_variables(scope_objects_incoming, incoming)
        for variable in free_variables_incoming:
            print("Variable incoming = "+variable)
            if variable not in free_variables:
                free_variables.append(variable)

        print("Complete list of free variables = "+str(free_variables))

    def get_free_variables(self, scope_objects, term):
        
        free_variables = []
        term_list = list(term)
        
        for scope in scope_objects[::-1]:
            print("Scope = "+str(scope))

            scope_string = ""
            i = scope.start_index
            while i < scope.end_index:
                scope_string = scope_string + term_list[i]
                i = i + 1
            
            free_variables_found = re.findall("[a-zA-Z]",scope_string)
            #Remove duplicate letters
            #print("Free variables = "+str(free_variables_found))
            free_variables_found = list(dict.fromkeys(free_variables_found))

            bound_variable_container = re.search("%(.*?)\.", term)
            if bound_variable_container is not None:
                bound_variable = bound_variable_container.group(1)
                print("Bound variable "+bound_variable+" found")
                #print("Bound variable = "+str(bound_variable))

                print("Free variables before = "+str(free_variables_found))
                free_variables_found.remove(bound_variable)
                print("Free variables after = "+str(free_variables_found))
            #print("New free variables = "+str(free_variables_found))

            print("Free variables found = "+str(free_variables_found))
            for variable in free_variables_found:
                free_variables.append(variable)

        free_variables = list(dict.fromkeys(free_variables))
        print("Free variables = "+str(free_variables))
        return free_variables


    def calculate_alpha(self):
        expression = input("Enter test expression: ")
        expression = self.check_brackets(expression)
        incoming = input("Enter incoming expression: ")
        incoming = self.check_brackets(incoming)

        if incoming is None or incoming == "None":
            #If there's nothing incoming, just alpha convert as normal
            scope_map, scope_objects = self.get_scopes(expression)
            self.test_print(scope_objects,expression)
            self.get_available_letters(expression, None)
            expression = self.rename_values(expression, scope_objects)
        else:
            scope_map_expression, scope_objects_expression = self.get_scopes(expression)
            scope_map_incoming, scope_objects_incoming = self.get_scopes(incoming)

            print("Expression scopes = ")
            self.test_print(scope_objects_expression, expression)
            print("Incoming scope = ")
            self.test_print(scope_objects_incoming, incoming)
            self.get_free_variables_with_incoming(scope_objects_expression,scope_objects_incoming, expression, incoming)
            self.get_available_letters(expression, incoming)
            expression = self.rename_values_with_incoming(expression, scope_objects_expression)
            expression = self.rename_values(expression, scope_objects_expression)

        return expression

if __name__ == "__main__":
    alpha_calculator = AlphaCalculatorFromComplete()
    expression = alpha_calculator.calculate_alpha()
    print(expression)

#this continually overrides replaced variables in smaller scopes, which means some letters aren't used when they should be
#this might become an issue in the future when I start looking at larger lambda terms, but for now... It works? So leave it?





