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

def analyse_value(abstraction, index, unchanged):
    bound_values = []

    # if abstraction[0] == '(':
    #     abstraction = abstraction[1:]
    # if abstraction[-1] == ')':
    #     abstraction = abstraction[:-1]

    print("Unchanged = "+unchanged)

    # firstDelPos=abstraction.find("(")
    # secondDelPos=abstraction.find(")")
    # if firstDelPos != -1 and secondDelPos != -1:
    #     abstraction = abstraction.replace(abstraction[firstDelPos:secondDelPos+1], " ")
    # print("After bracket checker: "+abstraction)

    abstraction_list = list(abstraction)
    for i, letter in enumerate(abstraction_list[:-1]):
        if letter == '%':
            bound_values.append(abstraction_list[i+1])

    if bound_values == []:
        return unchanged

    print(bound_values)

    abstraction_list = list(abstraction)
    for i,letter in enumerate(abstraction_list):
        if letter.isalpha():
            if letter not in bound_values:
                abstraction_list[i] = letter.upper()
    
    unchanged_list = list(unchanged)
    unchanged_list[index:index+len(abstraction_list)] = abstraction_list

    abstraction = "".join(abstraction_list)

    changed = "".join(unchanged_list)
    print("Changed string = "+changed)
    return changed

def main():

    #analyse_value("%x.x + yz (%y.yz)(%x.xz) + 3z")

    expression = input("Expression to test: ")
    print(str(len(expression)))

    exp_stack = Stack()
    index_stack = Stack()
    abstraction_list = []

    open_brackets = '('
    close_brackets = ')'

    new_expression = ""
    exp_stack.push(new_expression)
    expression_formatted = expression

    for i,c in enumerate(expression):
        if c == open_brackets:
            index_stack.push(i)
            new_expression = "("
            exp_stack.push(new_expression)
        elif c in close_brackets:
            abstraction = exp_stack.pop()
            abstraction = abstraction + ")"
            print("Analyse "+abstraction)
            expression_formatted = analyse_value(abstraction,index_stack.pop(),expression_formatted)
        else:
            expression = exp_stack.pop()
            expression = expression + c
            exp_stack.push(expression)
    
if __name__ == '__main__':
    main()