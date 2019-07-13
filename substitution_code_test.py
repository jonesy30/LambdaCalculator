import re
from AlphaCalculatorPartial import calculate_alpha

function = "[?/x][?/y]x"
expression = "y"

#FROM HERE
print("Before function = "+function)

bound_variables_left = re.findall("/(.*?)\]", function)

subst_container_match = re.search("\[(.*?)\]", function)
container = subst_container_match.group(0)
function = function.replace(container,"",1)

to_substitute = bound_variables_left[0]
bound_variables_left.pop(0)

end_value = len(function)
if len(bound_variables_left) > 0:
    #More than one bound variable -- do something here
    if to_substitute in bound_variables_left:
        #Bound variable repeated, need to check for the next instance of it
        for i,letter in enumerate(function):
            if letter == '[':
                subst_container_match = re.search("/(.*?)\]", function[i:])
                bound_value = subst_container_match.group(1)
                if to_substitute == bound_value:
                    break
        end_value = i
        function = calculate_alpha(to_substitute, function, expression, 0, end_value)
    else:
        function = calculate_alpha(to_substitute, function, expression)
else:
    function = calculate_alpha(to_substitute, function, expression)

new_function = function[:end_value].replace(to_substitute,expression) + function[end_value:]
print("New function = "+new_function)