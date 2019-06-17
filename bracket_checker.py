class Stack:

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()

expression = input("Expression to test: ")
print(expression)

exp_stack = Stack()

open_brackets = ['(','<','[','{']
close_brackets = [')','>',']','}']

for c in expression:
    if c in open_brackets:
        print("Open bracket found")
    elif c in close_brackets:
        print("Close brackets found")