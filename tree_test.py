class TreeNode(object):
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.children = []

    def add_child(self, obj, parent):
        child = TreeNode(obj, parent)
        self.children.append(child)
        return self.children[-1]
    
    def get_parent(self):
        return self.parent
    
    def append_data(self, new_data):
        self.data = self.data + new_data
    
    def get_data(self):
        return str(self.data)
    
    def print_level(self):
        #for child in self.children:
        #    print(child.data, end = '')
        if self.parent is not None:
            print(self.parent.children)

    #def get_level(self):
    #    return self.children

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
    
    def __repr__(self):
        return repr(self.data)
    
class Tree(object):
    def __init__(self):
        self.root = TreeNode("",None)
        self.deepest_node = root
    
    def get_root(self):
        return self.root
    
    def get_height(self):
        return self.root.get_height()


expression = input("Enter test expression: ")

t = Tree()
current_node = t.get_root()
current_node = current_node.add_child("",current_node)
for i,expression_letter in enumerate(expression):
    if expression_letter == '(':
        current_node.append_data(expression_letter)
        current_node = current_node.add_child("", current_node)
    elif expression_letter == ')':
        current_node = current_node.get_parent()
        current_node = current_node.get_parent()
        current_node = current_node.add_child("", current_node)
        current_node.append_data(expression_letter)
    else:
        current_node.append_data(expression_letter)

t.get_root().print_node()

print()
print("Level = ")
t.get_root().print_level()
print(str(t.get_height()))

t = Tree()
current_node = t.get_root().add_child(str(1),t.get_root())
current_node = current_node.add_child(str(2), current_node)
current_node.add_child(str(3), current_node)
current_node.add_child(str(3.5), current_node)
current_node = current_node.add_child(str(4), current_node)
print("Level printing")
current_node.print_level()

print()
t.get_root().print_node()
print()
print(str(t.get_height()))