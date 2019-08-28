import sys

#Class which alpha-converts a lambda term from within the evaluation (e.g. from a sub-term which only has one bound variable)

#Get the list of free variables in the expression
def get_free_variables(bound_value, expression):
    free_variables = []
    
    #Get the list of free variables by comparing each letter to the bound variable which has already been calculated by the calling class
    for letter in expression:
        if letter.isalpha() and letter != bound_value:
            free_variables.append(letter)
    
    #Return the list of free variables in the expression
    return free_variables

#Get the list of letters which could be used to replace conflicting variables, by removing all letters which are free from the alphabet
def get_available_letters(free_variables):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_list = list(alphabet)

    #For each of the free variables, remove it from the available_letters list and return
    for free_variable in free_variables:
        if free_variable in alphabet_list:
            alphabet_list.remove(free_variable)
    
    return alphabet_list

#Rename the relevant values in the expression to the available letters within the required substring
def rename_values(expression, free_variables, available_letters, start_value, end_value):
    available_letters = list(available_letters)
    replace_with = []
    
    #Find a list of replacements of the free variables from the list of available letters
    for variable in free_variables:
        new_letter = available_letters[0]
        replace_with.append(new_letter)
        available_letters.remove(new_letter)

    #Get the string to be converted in list form (so items can be replaced by index)
    expression_list = list(expression[start_value:end_value])
    for i,character in enumerate(expression_list):
        #If the character is a letter and it's in the free variables, replace it with the variable previously calculated
        if character.isalpha() and (character in free_variables):
            expression_list[i] = replace_with[free_variables.index(character)]
    
    #Get the new expression by joining the edited list of letters
    new_expression = "".join(expression_list)
    #Add any sections in the incoming expression which aren't to be processed to the final expression
    new_expression = expression[:start_value] + new_expression + expression[end_value:]
    #Return the alpha-converted expression
    return new_expression

#Main function which performs the alpha conversion
def calculate_alpha(bound_value, expression, incoming, start_value=0, end_value=None):

    #Remove the types of the incoming term (since alpha conversion and incoming types don't mix)
    incoming = remove_types(incoming)

    #Initialise values if the whole term is to be expressed
    if end_value == None:
        end_value = len(expression)        

    found_letter = False
    expression_list = list(expression)
    i = 0

    #Find the point in the string to start alpha converting (the first letter which appears which is less than the end_value)
    while found_letter == False and i < end_value:
        if expression_list[i].isalpha():

            #Get the list of free variables, the available letters which do not appear in the string
            #and use these to alpha-convert the term

            found_letter = True
            free_variables = get_free_variables(bound_value, incoming)
            available_letters = get_available_letters(free_variables)
            expression = rename_values(expression, free_variables, available_letters, start_value, end_value)
        i = i + 1
    
    return expression

#Function which removes the types of an incoming term (since types and alpha conversion don't mix)
def remove_types(output,end_value=None):
    bad_strings = [":int",":Int",":INT",":bool",":Bool",":BOOL",":None",":NONE",":none"]

    if end_value == None:
        modified = output
    else:
        modified = output[:end_value]

    modified = str(modified)
    for string in bad_strings:
        modified = modified.replace(string,"")

    if end_value != None:
        modified = modified + output[end_value:]

    return modified

#Function which is called if AlphaCalculatorPartial.py is called explicitly from the command line - this is for testing alone
if __name__ == "__main__":
    expression = calculate_alpha(sys.argv[1],sys.argv[2],sys.argv[3])
    print(expression)

#this continually overrides replaced variables in smaller scopes, which means some letters aren't used when they should be
#this might become an issue in the future when I start looking at larger lambda terms, but for now... It works? So leave it?

#This is for testing alone - it just prints a list of the scope objects
# for scope in scope_objects:
#     print()
#     print(scope.id)
    
#     scope_string = ""
#     i = scope.start_index
#     while i < scope.end_index:
#         scope_string = scope_string + expression[i]
#         i = i + 1
    
#     print(scope_string)





