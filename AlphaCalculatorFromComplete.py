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

    def rename_bound_values(self, expression):
        
        # for scope in scope_objects:
        #     #print("Scope = "+str(scope))
        #     term = ""
        #     i = scope.start_index
        #     while i < scope.end_index:
        #         term = term + expression[i]
        #         i = i + 1
        print("Incoming expression = "+str(expression))

        expression_list = list(expression)
        to_replace = self.get_bound_values(expression)

        replace_with = [""] * len(to_replace)
        for i,value_to_replace in enumerate(to_replace):
            other_bound_values = to_replace.copy()
            other_bound_values.remove(value_to_replace)
            if value_to_replace in other_bound_values:
                #If there are values left over
                replace_with[i] = self.available_letters[0]
                self.available_letters.remove(replace_with[i])
            else:
                replace_with[i] = value_to_replace 
            
        return to_replace,replace_with

        #     i = scope.start_index
        #     while i < scope.end_index:
        #         if expression[i] in to_replace:
        #             expression_list[i] = replace_with[to_replace.index(expression[i])]
        #         i = i + 1
            
        #     expression = "".join(expression_list)
        #     print("New expression = "+expression)

        # return expression

    def rename_free_values(self, expression, scope_objects):
        #Free is a value telling the function whether or not to do free variable conversion

        # for scope in scope_objects:
        #     #print("Scope = "+str(scope))
        #     term = ""
        #     i = scope.start_index
        #     while i < scope.end_index:
        #         term = term + expression[i]
        #         i = i + 1
        
        expression_list = list(expression)
        to_replace = self.free_variables(scope_objects,expression)
        to_replace = list(dict.fromkeys(to_replace))

        #Remove duplicates in free variables, just incase there are any still left
        replace_with = [""] * len(to_replace)
        for i,value_to_replace in enumerate(to_replace):
            replace_with[i] = self.available_letters[0]
            self.available_letters.remove(replace_with[i])

        return to_replace,replace_with
            # i = scope.start_index
            # while i < scope.end_index:
            #     if expression[i] in to_replace:
            #         expression_list[i] = replace_with[to_replace.index(expression[i])]
            #     i = i + 1
            
            # expression = "".join(expression_list)
            # print("New expression = "+expression)

        #return expression

    def rename_values(self, expression, scope_objects, free_variables=False):
        
        expression_list = list(expression)

        for scope in scope_objects:

            term = ""
            i = scope.start_index
            while i < scope.end_index:
                term = term + expression[i]
                i = i + 1

            if free_variables == True:
                to_replace, replace_with = self.rename_free_values(expression, scope_objects)
            else:
                to_replace, replace_with = self.rename_bound_values(expression)


            i = scope.start_index
            while i < scope.end_index:
                if expression[i] in to_replace:
                    expression_list[i] = replace_with[to_replace.index(expression[i])]
                i = i + 1
            
            expression = "".join(expression_list)

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

    def get_free_variables(self, scope_objects_expression, scope_objects_incoming, expression, incoming):

        free_variables = []
        free_variables_expression = self.free_variables(scope_objects_expression, expression)
        for variable in free_variables_expression:
            print("Variable expression = "+variable)
            free_variables.append(variable)

        free_variables_incoming = self.free_variables(scope_objects_incoming, incoming)
        for variable in free_variables_incoming:
            print("Variable incoming = "+variable)
            if variable not in free_variables:
                free_variables.append(variable)

        print("Complete list of free variables = "+str(free_variables))

    def free_variables(self, scope_objects, term):
        
        free_variables = []
        term_list = list(term)
        
        for scope in scope_objects[::-1]:
            #print("Scope = "+str(scope))

            scope_string = ""
            i = scope.start_index
            while i < scope.end_index:
                scope_string = scope_string + term_list[i]
                i = i + 1
            
            free_variables_found = re.findall("[a-zA-Z]",scope_string)
            #Remove duplicate letters
            free_variables_found = list(dict.fromkeys(free_variables_found))

            bound_variable_container = re.search("%(.*?)\.", term)
            if bound_variable_container is not None:
                bound_variable = bound_variable_container.group(1)
                if bound_variable in free_variables_found:
                    free_variables_found.remove(bound_variable)

            for variable in free_variables_found:
                free_variables.append(variable)

        free_variables = list(dict.fromkeys(free_variables))
        return free_variables

    def calculate_alpha(self, expression, incoming):

        if incoming is None or incoming == "None":
            #If there's nothing incoming, just alpha convert as normal
            scope_map, scope_objects = self.get_scopes(expression)
            self.test_print(scope_objects,expression)
            self.get_available_letters(expression, None)
            expression = self.rename_values(expression, scope_objects,False)
        else:
            scope_map_expression, scope_objects_expression = self.get_scopes(expression)
            scope_map_incoming, scope_objects_incoming = self.get_scopes(incoming)

            #print("Expression scopes = ")
            #self.test_print(scope_objects_expression, expression)
            #print("Incoming scope = ")
            #self.test_print(scope_objects_incoming, incoming)
            self.get_free_variables(scope_objects_expression,scope_objects_incoming, expression, incoming)  
            self.get_available_letters(expression, incoming)

            expression = self.rename_values(expression, scope_objects_expression,True)
            expression = self.rename_values(expression, scope_objects_expression,False)

        print("Returning expression in calculate alpha "+expression)
        return expression

if __name__ == "__main__":   
    alpha_calculator = AlphaCalculatorFromComplete()

    expression = input("Enter test expression: ")
    expression = alpha_calculator.check_brackets(expression)
    incoming = input("Enter incoming expression: ")
    incoming = alpha_calculator.check_brackets(incoming)

    expression = alpha_calculator.calculate_alpha(expression, incoming)
    print(expression)

#this continually overrides replaced variables in smaller scopes, which means some letters aren't used when they should be
#this might become an issue in the future when I start looking at larger lambda terms, but for now... It works? So leave it?





