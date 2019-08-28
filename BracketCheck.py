from Stack import Stack

#Class taken from https://www.sanfoundry.com/python-program-implement-stack/

#Class which checks that the brackets match, all open brackets are closed and all closed brackets have corresponding opens

class BracketCheck:
    def check_brackets(self,expression):

        #Use a stack to check each close bracket matches a current open bracket
        exp_stack = Stack()

        #A list of all closed and open brackets
        open_brackets = ['(','[','{']
        close_brackets = [')',']','}']

        matched_brackets = True

        #For each character in the expression
        for c in expression:
            #Push open brackets to the stack if come across
            if c in open_brackets:
                exp_stack.push(c)
            #If a close bracket is come across, pop the bracket stack
            #If there is an error, there was no matching open bracket and so the brackets are mismatched
            elif c in close_brackets:
                popped = exp_stack.pop()
                if popped == -1:
                    matched_brackets = False
                    break
                #If the brackets don't match, for example ) being used to close a [, this is also an error
                if(open_brackets.index(popped) != close_brackets.index(c)):
                    matched_brackets = False
                    break

        #If there are any open brackets left over in the stack, this is also an issue (since not all open brackets have been closed)
        if(exp_stack.pop() != -1):
            matched_brackets = False

        #Return whether or not the brackets are properly matched
        return matched_brackets