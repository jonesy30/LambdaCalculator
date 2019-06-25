#Class taken from https://www.sanfoundry.com/python-program-implement-stack/
class Stack:

    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if(len(self.stack) != 0):
            return self.stack.pop()
        return -1

expression = input("Expression to test: ")

exp_stack = Stack()
abstraction_list = []

open_brackets = '('
close_brackets = ')'

new_expression = ""
exp_stack.push(new_expression)

for c in expression:
    if c == open_brackets:
        new_expression = ""
        exp_stack.push(new_expression)
    elif c in close_brackets:
        print("Analyse "+exp_stack.pop())
    else:
        expression = exp_stack.pop()
        expression = expression + c
        exp_stack.push(expression)