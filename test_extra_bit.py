import re
import sys

test_string = "x:int+x:int"
test_string_2 = "x+x"

bound_variable = "x"
type = "int"

function_list = list(test_string)
for i,character in enumerate(function_list):
    if character == bound_variable:

        if function_list[i+1] == ":":
            print("IGNORE")
        else:
            function_list[i] = character + ":" + type
    
processed_function = "".join(function_list)
print("Processed function = "+str(processed_function))