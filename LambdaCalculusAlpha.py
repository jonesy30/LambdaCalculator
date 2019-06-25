import sys
from antlr4 import *
from LambdaCalculusLexer import LambdaCalculusLexer
from LambdaCalculusParser import LambdaCalculusParser
from LambdaCalculusListener import LambdaCalculusListener

from sympy.solvers import solve
from sympy import Symbol

def main():
    abstraction = input("Enter abstraction: ")

    bound_value = None

    if abstraction[0] == '(':
        abstraction = abstraction[1:]
    if abstraction[-1] == ')':
        abstraction = abstraction[:-1]
    
    if abstraction[0] == '%':
        bound_value = abstraction[1]
        print("Bound value = "+bound_value)
    else :
        print("Nothing found!!")
        sys.exit(0)
    
    firstDelPos=abstraction.find("(")
    secondDelPos=abstraction.find(")")
    if firstDelPos != None and secondDelPos != None:
        abstraction = abstraction.replace(abstraction[firstDelPos:secondDelPos+1], "")
    print("After bracket checker: "+abstraction)

    abstraction_list = list(abstraction)
    for i,letter in enumerate(abstraction_list):
        if letter.isalpha():
            if letter != bound_value:
                abstraction_list[i] = letter.upper()
    
    abstraction = "".join(abstraction_list)
    print("New abstraction = "+abstraction)

if __name__ == '__main__':
    main()