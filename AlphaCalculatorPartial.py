import sys

def get_free_variables(bound_value, expression):
    free_variables = []
    
    for letter in expression:
        if letter.isalpha() and letter != bound_value:
            free_variables.append(letter)
    
    return free_variables

def get_available_letters(free_variables):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_list = list(alphabet)

    for free_variable in free_variables:
        if free_variable in alphabet_list:
            alphabet_list.remove(free_variable)
    
    return alphabet_list

def rename_values(expression, free_variables, available_letters, start_value, end_value):
    available_letters = list(available_letters)
    replace_with = []
    
    for variable in free_variables:
        new_letter = available_letters[0]
        replace_with.append(new_letter)
        available_letters.remove(new_letter)

    expression_list = list(expression[start_value:end_value])
    for i,character in enumerate(expression_list):
        if character.isalpha() and (character in free_variables):
            expression_list[i] = replace_with[free_variables.index(character)]
    
    new_expression = "".join(expression_list)
    new_expression = expression[:start_value] + new_expression + expression[end_value:]
    return new_expression

def calculate_alpha(bound_value, expression, incoming, start_value = 0, end_value = None):

    if end_value == None:
        end_value = len(expression)        

    found_letter = False
    expression_list = list(expression)
    i = 0

    while found_letter == False and i < end_value:
        if expression_list[i].isalpha():
            found_letter = True
            free_variables = get_free_variables(bound_value, incoming)
            available_letters = get_available_letters(free_variables)
            expression = rename_values(expression, free_variables, available_letters, start_value, end_value)
        i = i + 1
    
    return expression

if __name__ == "__main__":
    expression = calculate_alpha(sys.argv[1],sys.argv[2],sys.argv[3])
    print(expression)

#this continually overrides replaced variables in smaller scopes, which means some letters aren't used when they should be
#this might become an issue in the future when I start looking at larger lambda terms, but for now... It works? So leave it?

#This is for testing alone
# for scope in scope_objects:
#     print()
#     print(scope.id)
    
#     scope_string = ""
#     i = scope.start_index
#     while i < scope.end_index:
#         scope_string = scope_string + expression[i]
#         i = i + 1
    
#     print(scope_string)





