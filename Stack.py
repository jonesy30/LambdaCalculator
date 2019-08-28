#taken from https://www.sanfoundry.com/python-program-implement-stack/
#Just a basic Stack class which is used many times throughout the lambda evaluation

class Stack:

    #Initialise the stack
    def __init__(self):
        self.items = []
    
    #Return whether or not there are items in the stack
    def is_empty(self):
        return self.items == []
    
    #Push an item to the stack list
    def push(self, data):
        self.items.append(data)
    
    #Pop an item from the stack list
    def pop(self):
        if self.is_empty():
            return -1
        return self.items.pop()
    
    #Get the length of the stack
    def get_size(self):
        return len(self.items)