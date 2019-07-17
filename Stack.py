#taken from https://www.sanfoundry.com/python-program-implement-stack/
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if self.is_empty():
            return -1
        return self.items.pop()