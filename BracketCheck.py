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

class BracketCheck:
    def check_brackets(self,expression):

        exp_stack = Stack()

        open_brackets = ['(','[','{']
        close_brackets = [')',']','}']

        matched_brackets = True

        for c in expression:
            if c in open_brackets:
                exp_stack.push(c)
            elif c in close_brackets:
                popped = exp_stack.pop()
                if popped == -1:
                    matched_brackets = False
                    break
                if(open_brackets.index(popped) != close_brackets.index(c)):
                    matched_brackets = False
                    break

        if(exp_stack.pop() != -1):
            matched_brackets = False

        return matched_brackets