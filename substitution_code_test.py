import re
from AlphaCalculatorPartial import calculate_alpha

#function = "[?/x][?/z] + x[?/x]x+y+z"
#function = "[?/x]9x+y[?/x][?/z]x"
function = "[?/x][?/x]x"
#function = "[?/x][?/x][?/z]x+2"
#function = "[?/x][?/y]x+y+z"

expression = "3"
print("Original function = "+function)

bound_variables = re.findall("/(.*?)\]", function)
print("Bound_variables = "+str(bound_variables))

subst_container_match = re.search("\[(.*?)\]", function)
container = subst_container_match.group(0)
function = function.replace(container,"",1)
print("Function now = "+function)

to_substitute = bound_variables[0]
bound_variables.pop(0)

bound_variables_left = bound_variables

print("Substiture = "+to_substitute)
print("Bound_variables now = "+str(bound_variables_left))

end_value = len(function)
if len(bound_variables_left) > 0:
    print("More than one bound variable -- do something here")
    if to_substitute in bound_variables_left:
        print("Need to do something complex here - bound variable repeated")
        for i,letter in enumerate(function):
            print("Letter = "+letter+" at "+str(i))
            if letter == '[':
                subst_container_match = re.search("/(.*?)\]", function[i:])
                bound_value = subst_container_match.group(1)
                print("Bound value = "+bound_value)
                if to_substitute == bound_value:
                    print("Match!!")
                    break
        end_value = i
        print("End i = "+str(end_value))
        print("To process: "+function[:end_value])
        function = calculate_alpha(to_substitute, function, expression, 0, end_value)
    else:
        print("Old functon = "+function)
        function = calculate_alpha(to_substitute, function, expression)
        print("New function = "+function)
else:
    print("Old functon = "+function)
    function = calculate_alpha(to_substitute, function, expression)
    print("New function = "+function)

print("Before replacing "+function)
print("To substitute = "+to_substitute)

print("I'm almost there... Just need to work out how to only replace before a certain value")
new_function = function[:end_value].replace(to_substitute,expression) + function[end_value:]
 
#What if longer

print("After replacing = "+new_function)

# subst_container_match = re.search("\[(.*?)\]", function)
# container = subst_container_match.group(0)
# function = function.replace(container,"",1)
# print("Function after extracton + "+function)

# bound_variable_match = re.search("/(.*?)\]", container)
# bound_variable = bound_variable_match.group(1)

#get all bound variables found in [?/bound_variable]function
#bound_variable = re.findall("/(.*?)\]", function)
#match = re.search("/(.*?)\]", function)
#get the first group (the inner bit of the regex) which matches this expression -- outermost first
#bound_variable = match.group(1)
#NOTE: I need to find a way of only getting rid of the first bit
#function = re.sub("\[(.*?)\]","",function)

# print("Bound variable = "+bound_variable)

# print("Function after = "+str(function))
# expression = ctx.getChild(1).getText()
# ##print("Function before = "+function)
# function = calculate_alpha(bound_variable,function, expression)
# ##print("Function after = "+function)
# print("Bound variable through abstraction = "+str(bound_variable))
# print("Function through abstraction = "+str(function))
# print("Expression through abstraction = "+str(expression))

# new_function = function.replace(bound_variable,expression)
# print("New function = "+new_function)