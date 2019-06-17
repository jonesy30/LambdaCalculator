import sys

#Class taken from https://www.sanfoundry.com/python-program-implement-stack/
class Stack:

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if(len(self.items) != 0):
            return self.items.pop()
        return -1

expression = input("Expression to test: ")

exp_stack = Stack()

open_brackets = ['(','<','[','{']
close_brackets = [')','>',']','}']

matched_brackets = True

for c in expression:
    if c in open_brackets:
        exp_stack.push(c)
    elif c in close_brackets:
        popped = exp_stack.pop()
        #Need to work out how to deal with the value not being in the list
        if popped == -1:
            matched_brackets = False
            break
        if(open_brackets.index(popped) != close_brackets.index(c)):
            matched_brackets = False
            break


if(exp_stack.pop() != -1):
    matched_brackets = False

if matched_brackets == True:
    print("Matched brackets")
else:
    print("Unmatched brackets")