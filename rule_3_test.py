import re
from AlphaCalculatorPartial import calculate_alpha

function = "[?/x][?/x][?/x]x"
incoming = 3

function_list = []
print("Function before extraction: "+function)
subst_container_match = re.search("\[(.*?)\]", function)
container = subst_container_match.group(0)
function = function.replace(container,"",1)
print("Function after extracton: "+function)
function_list.append(function)
re.purge()
subst_container_match = re.search("\[(.*?)\]", function)

while subst_container_match is not None:
    container = subst_container_match.group(0)
    function = function.replace(container,"",1)
    print("Function after extraction: "+function)
    function_list.append(function)
    re.purge()
    subst_container_match = re.search("\[(.*?)\]", function)  

print("Function list = "+str(function_list))

i = len(function_list) - 2
while i > -1:
    print("i = "+str(i))
    extracted_function = function_list[i]
    print("Extracted function = "+extracted_function)

    bound_variable_match = re.search("/(.*?)\]", extracted_function)
    bound_variable = bound_variable_match.group(1)

    extracted_function = calculate_alpha(bound_variable, extracted_function, bound_variable)
    function_list[i] = extracted_function
    i = i - 1

print("New function list = "+str(function_list))

#get all bound variables found in [?/bound_variable]function
#bound_variable = re.findall("/(.*?)\]", function)
#match = re.search("/(.*?)\]", function)
#get the first group (the inner bit of the regex) which matches this expression -- outermost first
#bound_variable = match.group(1)
#NOTE: I need to find a way of only getting rid of the first bit
#function = re.sub("\[(.*?)\]","",function)