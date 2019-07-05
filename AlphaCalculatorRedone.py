from BracketCheck import BracketCheck
import sys

#taken from https://www.sanfoundry.com/python-program-implement-stack/
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()
    
class TreeNode(object):
    def __init__(self,data,parent):
        self.data = data
        self.parent = parent
        self.children = []
        self.bracket_stack = Stack()
    
    def get_grandparent(self):
        print("Leaving child "+self.data + ", going to "+self.parent.parent.data)
        return self.parent.parent
    
    def get_siblings(self):
        siblings = None
        if self.parent is not None:
            siblings = []
            for child in self.parent.children:
                siblings.append(child)
            
        return siblings
    
    def add_child(self, data, parent):
        print("Adding child "+data)
        child = TreeNode(data, parent)
        self.children.append(child)
        return self.children[-1]
    
    def append_data(self, data):
        print("Appending data "+data)
        self.data = self.data + data

    def to_string(self):
        string = self.data
        for child in self.children:
            string = string + "\n" + str(child.to_string())

        return string

class Tree(object):
    def __init__(self):
        self.root = TreeNode("RootNode",None)
        self.current_node = self.root
    
    def get_root(self):
        return self.root

    def add_child(self, data):
        self.current_node = self.current_node.add_child(data,self.current_node)
    
    def exit_child(self):
        self.current_node = self.current_node.get_parent()
    
    def append_data(self, new_data):
        self.current_node = self.current_node.append_data(new_data)
        if data == '(':
            self.current_node.bracket_stack.push(data)
        elif data == ')':
            if not self.current_node.bracket_stack.is_empty():
                self.current_node.bracket_stack.pop()
                return self
            else:
                for sibling in self.current_node.get_siblings():
                    if not sibling.bracket_stack.is_empty():
                        sibling.bracket_stack.pop()
                        return self
                grandparent = self.get_grandparent()
                #return grandparent.add_child("",grandparent)
                return grandparent

bracket_checker = BracketCheck()

expression = input("Enter test expression: ")
matched_brackets = bracket_checker.check_brackets(expression)

while matched_brackets == False:
    expression = input("Sorry, mismatched brackets, check and try again?")
    matched_brackets = bracket_checker.check_brackets(expression)

#ToDo: Find and rename bound variables
#Step 1: Determine the scope of a lambda term
#Step 2: Find bound variables
#Step 3: Find something to rename them to
#Step 4: Rename them

bracket_stack = Stack()
t = Tree()
t.add_child("Second root node")

for expression_letter in expression:
        if expression_letter == '%':
            t.add_child("%")
        else:
            t.append_data(expression_letter)

print(t.get_root().to_string())



