from ScopeObject import ScopeObject
from CurrentLetter import CurrentLetter

class TreeNode(object):
    def __init__(self, data, parent, sibling_scope_object, current_letter):
        self.data = data
        self.parent = parent
        self.children = []
        self.sibling_scope_object = sibling_scope_object
        self.current_letter = current_letter
        self.processed_data = None

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
    
    def get_siblings(self):
        siblings = None
        if self.parent is not None:
            siblings = []
            for child in self.parent.children:
                siblings.append(child)
            
        return siblings

    def print_node(self):
        print(self.data, end = '')
        for child in self.children:
            child.print_node()
    
    def get_height(self):
        height_list = []
        if self.children == []:
            return 0
        for child in self.children:
            child_height = child.get_height()
            height_list.append(child_height)
        return max(height_list) + 1

    def get_bound_values(self, data):
        bound_values = []
        if data is not None:
            abstraction_list = list(data)
            for i, letter in enumerate(abstraction_list[:-1]):
                if letter == '%':
                    bound_values.append(abstraction_list[i+1])
        
        #if bound_values == []:
        #    return self.data

        return bound_values
    
    def process_abstraction(self, data, scope_object):
        print("Data = "+data)
        abstraction_list = list(data)

        for i,letter in enumerate(abstraction_list):
            if letter.isalpha():
                if letter not in scope_object.original_letters:
                    print("LETTER "+letter+" NOT IN FOUND VALUES")
                else:
                    abstraction_list[i] = scope_object.associated_letters[scope_object.original_letters.index(letter)]

        abstraction = "".join(abstraction_list)
        return abstraction
    
    def process_level(self, level):

        level_list = []
        if level is not None:
            for sibling in level:
                for letter in sibling.data:
                    level_list.append(letter)
            #level_list = list(level)
        
        for i,letter in enumerate(level_list):
            if letter.isalpha():
                if letter not in self.sibling_scope_object.bound_values:
                    if letter not in self.sibling_scope_object.original_letters:

                        #print(letter+" not found")
                        #print("Original_letters "+str(self.sibling_scope_object.original_letters))
                        #print("Associated_letters "+str(self.sibling_scope_object.associated_letters))

                        self.sibling_scope_object.original_letters.append(letter)
                        new_letter = self.sibling_scope_object.current_letter.getUpperCase()
                        self.sibling_scope_object.associated_letters.append(new_letter)
                else:
                    if letter not in self.sibling_scope_object.original_letters:

                        #print(letter+" not found")
                        #print("Original_letters "+str(self.sibling_scope_object.original_letters))
                        #print("Associated_letters "+str(self.sibling_scope_object.associated_letters))

                        self.sibling_scope_object.original_letters.append(letter)
                        new_letter = self.sibling_scope_object.current_letter.getLowerCase()
                        self.sibling_scope_object.associated_letters.append(new_letter)
        

    def process_node(self):
        print()
        print()
        print("Processing node")

        returned_bound_values = self.get_bound_values(self.print_siblings())
        #scope_object = ScopeObject(current_letter)
        self.sibling_scope_object.bound_values = returned_bound_values
        self.process_level(self.get_siblings())
        print("Me = "+str(self.data))
        print("Level = "+str(self.print_siblings()))
        print("Original letters = "+str(self.sibling_scope_object.original_letters))
        print("Associated letters = "+str(self.sibling_scope_object.associated_letters))
        print("Processed_data = "+str(self.processed_data))
        #children_print = self.process_abstraction(self.data, self.sibling_scope_object)
       

        if self.processed_data == None:
            siblings = self.get_siblings()
            if siblings is not None:
                for sibling in siblings:
                    sibling.processed_data = self.process_abstraction(sibling.data,self.sibling_scope_object)
                    #abstraction = sibling.process_node()
                    #if abstraction is not None:
                    #    abstraction_full = abstraction_full + abstraction

        if self.processed_data == None:
            abstraction_full = self.process_abstraction(self.data, self.sibling_scope_object)
        else:
            abstraction_full = self.processed_data
            
        for child in self.children:
           abstraction = child.process_node()
           if abstraction is not None:
               abstraction_full = abstraction_full + abstraction
        #return children_print

        return abstraction_full

        
    def __repr__(self):
        return repr(self.data)
    
class Tree(object):
    def __init__(self, current_letter):
        s = ScopeObject(current_letter)
        self.root = TreeNode("",None,s,current_letter)
        self.height = 0
        self.levels = []
        self.current_node = self.root
    
    def get_root(self):
        return self.root

    def get_node(self):
        return str(self.current_node.data)
    
    def get_height(self):
        return self.root.get_height()
    
    def add_child(self, data):
        self.current_node = self.current_node.add_child(data,self.current_node)
    
    def exit_child(self):
        self.current_node = self.current_node.get_parent()
    
    def append_data(self, new_data):
        self.current_node.data = self.current_node.data + new_data

expression = input("Enter test expression: ")

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

t.get_root().print_node()
print()
print("Processed node")


print(t.get_root().process_node())

# print()
# print("Level = ")
# t.get_root().print_level()
# print(str(t.get_height()))

# t = Tree()
# current_node = t.get_root().add_child(str(1),t.get_root())
# current_node = current_node.add_child(str(2), current_node)
# current_node.add_child(str(3), current_node)
# current_node.add_child(str(3.5), current_node)
# current_node = current_node.add_child(str(4), current_node)
# print("Level printing")
# current_node.print_level()

# print()
# t.get_root().print_node()
# print()
# print(str(t.get_height()))