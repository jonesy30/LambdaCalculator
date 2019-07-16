from BracketCheck import BracketCheck
import sys

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()

    def __repr__(self):
        return str(self.items)

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

#Look for the letter after the lambda (%) operator to find the variables bound in the current scope
def get_bound_values(data):
    bound_values = []
    if data is not None:
        abstraction_list = list(data)
        for i, letter in enumerate(abstraction_list[:-1]):
            if letter == '%':
                bound_values.append(abstraction_list[i+1])
    
    return bound_values

#Method to make sure the brackets are all matched up in the string the user has entered
def check_brackets():
    bracket_checker = BracketCheck()

    expression = input("Enter test expression: ")
    matched_brackets = bracket_checker.check_brackets(expression)

    while matched_brackets == False:
        expression = input("Sorry, mismatched brackets, check and try again?")
        matched_brackets = bracket_checker.check_brackets(expression)
    
    return expression

#Method to create a map of each letter according to their scope ids, and a list of scopes those ids represent
def get_scopes(expression):
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
            while current_scope.brackets.isEmpty():
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

def rename_values(expression,scope_map,scope_objects):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    available_letters = list(alphabet)

    #for scope in reversed(scope_objects):
    # for scope in scope_objects:
    #     term = ""
    #     i = scope.start_index
    #     while i < scope.end_index:
    #         term = term + expression[i]
    #         i = i + 1

    #     expression_list = list(expression)    
    #     bound_values = get_bound_values(term)
    #     print("Term = "+term)
    #     print("Bound_values = "+str(bound_values))

    #     replace_with = [""] * len(bound_values)
    #     for i,bound_value in enumerate(bound_values):
    #         if bound_value not in available_letters:
    #             replace_with[i] = available_letters[0]
    #         else:
    #             replace_with[i] = bound_value
    #         available_letters.remove(replace_with[i])
    #         print("Replacing "+bound_value+" with "+replace_with[i])

    #     i = scope.start_index
    #     while i < scope.end_index:
    #         if expression[i] in bound_values:
    #             #expression_list[i] = expression_list[i].upper()
    #             expression_list[i] = replace_with[bound_values.index(expression[i])]
    #         i = i + 1
    #     expression = "".join(expression_list)

    #for scope in reversed(scope_objects):
    for scope in scope_objects:
        term = ""
        i = scope.start_index
        while i < scope.end_index:
            term = term + expression[i]
            i = i + 1
    
        expression_list = list(expression)
        bound_values = get_bound_values(expression)
        print("Bound values = "+str(bound_values))

        replace_with = [""] * len(bound_values)
        for i,bound_value in enumerate(bound_values):
            other_bound_values = bound_values
            other_bound_values.remove(bound_value)
            if bound_value in other_bound_values:
                print("Other bound values")
                replace_with[i] = available_letters[0]
                print("Replacing "+str(i)+" with "+replace_with[i])
                available_letters.remove(replace_with[i])

            else:
                replace_with[i] = bound_value

        i = scope.start_index
        while i < scope.end_index:
            if expression[i] in bound_values:
                #expression_list[i] = expression_list[i].upper()
                expression_list[i] = replace_with[bound_values.index(expression[i])]
            i = i + 1
        
        expression = "".join(expression_list)
        print("New expression = "+expression)

    return expression

#This is for testing alone
def test_print(scope_objects,expression):

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

#ToDo: Find and rename bound variables
#Step 1: Determine the scope of a lambda term (done)
#Step 2: Find bound variables (done)
#Step 3: Find something to rename them to (done)
#Step 4: Rename them (also done)

def calculate_alpha():
    expression = check_brackets()

    scope_map, scope_objects = get_scopes(expression)
    test_print(scope_objects,expression)
    expression = rename_values(expression, scope_map, scope_objects)
    return expression

if __name__ == "__main__":
    expression = calculate_alpha()
    print(expression)

#this continually overrides replaced variables in smaller scopes, which means some letters aren't used when they should be
#this might become an issue in the future when I start looking at larger lambda terms, but for now... It works? So leave it?





