class TreeNode(object):
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.children = []

    def add_child(self, data, parent):
        child = TreeNode(data, parent)
        self.children.append(child)
        return self.children[-1]
    
    def get_parent(self):
        return self.parent
    
    # def append_data(self, new_data):
    #     self.data = self.data + new_data
    
    def print_level(self):
        if self.parent is not None:
            output = ""
            for child in self.parent.children:
                output = output + str(child)
            
            return output

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
            bound_values = []
            abstraction_list = list(data)
            for i, letter in enumerate(abstraction_list[:-1]):
                if letter == '%':
                    bound_values.append(abstraction_list[i+1])

            if bound_values == []:
                return self.data

        return bound_values
    
    def process_abstraction(self, data, bound_values):
        abstraction_list = list(data)
        for i,letter in enumerate(abstraction_list):
            if letter.isalpha():
                if letter not in bound_values:
                    abstraction_list[i] = letter.upper()
        
        abstraction = "".join(abstraction_list)
        return abstraction

    def process_node(self):
        #print(self.data)

        #if self.children == []:
        #    self.process_abstraction(self.data)
        bound_values = self.get_bound_values(self.print_level())

        children_print = self.process_abstraction(self.data, bound_values)
        for child in self.children:
            abstraction = child.process_node()
            children_print = children_print + abstraction
        return children_print
        
        
        
    def __repr__(self):
        return repr(self.data)
    
class Tree(object):
    def __init__(self):
        self.root = TreeNode("",None)
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

t = Tree()
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