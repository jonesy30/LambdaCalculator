from ScopeObject import ScopeObject
from CurrentLetter import CurrentLetter
from BracketCheck import BracketCheck
import sys

#Class which represents a node in the tree - each node is a substring of the total expression
class TreeNode(object):
    def __init__(self, data, parent, sibling_scope_object, current_letter):
        self.data = data
        self.parent = parent
        self.children = []
        self.sibling_scope_object = sibling_scope_object
        self.current_letter = current_letter
        self.processed_data = None

        #sibling_scope_object: information about the current scope which gets passed to my siblings (they're in the same scope as me)
        #current letter: a class using the singleton pattern which keeps track of which letter you're currently on
            #(a is used to replace, then b, then c, etc.)
        #processed data: the converted version of the string this node represents

    def add_child(self, data, parent):
        s = ScopeObject(self.current_letter)
        child = TreeNode(data, parent, s, self.current_letter)
        self.children.append(child)
        return self.children[-1]
    
    def get_parent(self):
        return self.parent
    
    def print_siblings(self):
        if self.parent is not None:
            output = ""
            for child in self.parent.children:
                output = output + str(child)
            
            return output
    
    #Get all nodes on the same level as me (my siblings) - these are all within my scope and so need the same variable namings
    def get_siblings(self):
        siblings = None
        if self.parent is not None:
            siblings = []
            for child in self.parent.children:
                siblings.append(child)
            
        return siblings

    #Look for the letter after the lambda (%) operator to find the variables bound in the current scope
    def get_bound_values(self, data):
        bound_values = []
        if data is not None:
            abstraction_list = list(data)
            for i, letter in enumerate(abstraction_list[:-1]):
                if letter == '%':
                    bound_values.append(abstraction_list[i+1])
        
        return bound_values
    
    #Replace all values with their new names
    def process_abstraction(self, data, scope_object):
        abstraction_list = list(data)

        for i,letter in enumerate(abstraction_list):
            if letter.isalpha():
                if letter not in scope_object.original_letters:
                    print("LETTER "+letter+" NOT IN FOUND VALUES")
                else:
                    abstraction_list[i] = scope_object.associated_letters[scope_object.original_letters.index(letter)]

        abstraction = "".join(abstraction_list)
        return abstraction
    
    #Process siblings at the same time as me so they get the same names - they're in my scope
    def process_siblings(self, siblings):

        sibling_list = []
        if siblings is not None:
            for sibling in siblings:
                for letter in sibling.data:
                    sibling_list.append(letter)
        
        for i,letter in enumerate(sibling_list):
            if letter.isalpha():
                #bound variables get lowercase letters, unbound get uppercase
                if letter not in self.sibling_scope_object.original_letters:
                    self.sibling_scope_object.original_letters.append(letter)
                    if letter not in self.sibling_scope_object.bound_values:
                        new_letter = self.sibling_scope_object.current_letter.getUpperCase()
                    else:
                        new_letter = self.sibling_scope_object.current_letter.getLowerCase()
                    self.sibling_scope_object.associated_letters.append(new_letter)

    #Process me (and my siblings if I haven't been processed yet)
    def process_node(self):

        returned_bound_values = self.get_bound_values(self.print_siblings())
        self.sibling_scope_object.bound_values = returned_bound_values
        self.process_siblings(self.get_siblings())

        #if I have not been processed, process me and my siblings
        if self.processed_data == None:
            siblings = self.get_siblings()
            if siblings is not None:
                for sibling in siblings:
                    sibling.processed_data = self.process_abstraction(sibling.data,self.sibling_scope_object)
            
            abstraction_full = self.process_abstraction(self.data, self.sibling_scope_object)
        else:
            abstraction_full = self.processed_data

        #process my children
        for child in self.children:
           abstraction = child.process_node()
           if abstraction is not None:
               abstraction_full = abstraction_full + abstraction

        return abstraction_full

    def __repr__(self):
        return repr(self.data)
    
#class which is the tree structure for this scope tree
class Tree(object):
    def __init__(self, current_letter):
        s = ScopeObject(current_letter)
        self.root = TreeNode("",None,s,current_letter)
        self.current_node = self.root
    
    def get_root(self):
        return self.root

    def add_child(self, data):
        self.current_node = self.current_node.add_child(data,self.current_node)
    
    def exit_child(self):
        self.current_node = self.current_node.get_parent()
    
    def append_data(self, new_data):
        self.current_node.data = self.current_node.data + new_data

def calculate_alpha():
    bracket_checker = BracketCheck()

    expression = input("Enter test expression: ")
    matched_brackets = bracket_checker.check_brackets(expression)

    while matched_brackets == False:
        expression = input("Sorry, mismatched brackets, check and try again?")
        matched_brackets = bracket_checker.check_brackets(expression)

    #Create the scope tree with the expression input by the user
    current_letter = CurrentLetter()
    t = Tree(current_letter)
    t.add_child("")
    for i,expression_letter in enumerate(expression):
        if expression_letter == '(':
            t.append_data(expression_letter)
            t.add_child("")
        elif expression_letter == ')':
            t.exit_child()
            t.exit_child()
            t.add_child("")
            t.append_data(expression_letter)
        else:
            t.append_data(expression_letter)

    output = t.get_root().process_node()
    return output

if __name__ == '__main__':
    output = calculate_alpha()
    print(output)
