import pytest
import sys
sys.path.append("..")
from LambdaCalculus import unit_t_interface

#Python file containing unit tests for the program

#Testing the call_by_value beta reduction method by testing it with a lambda term that does have a normal form in
#call_by_name but NOT in call_by_value
def test_call_by_value():

    expression = "(%x.%y.y)((%z.zz)(%z.zz))"
    output_expected = "cannot be found"

    output_returned = unit_t_interface(expression,"v")

    output_actual = output_returned

    assert output_expected in output_actual,"test failed because returned = "+str(output_actual)

#Testing the call_by_name beta reduction method by testing it with a lambda term that does have a normal form in
#call_by_name but NOT in call_by_value
def test_call_by_name():

    expression = "(%x.%y.y)((%z.zz)(%z.zz))"
    output_expected = "(%y.y)"

    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        output_actual = output_returned[0]

    assert output_expected in output_actual,"test failed because returned = "+str(output_actual)

#Testing both beta-reduction strategies by testing the code with a term with nested applications
def test_multi_input():

    expression = "(%b.b+(%a.a+b)3)4"
    output_expected = "11"

    #Test call-by-name
    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        output_actual = output_returned[0]

    assert output_expected in output_actual,"test failed because returned = "+str(output_actual)

    #Test call-by-value
    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        output_actual = output_returned[0]

    assert output_expected in output_actual,"test failed because returned = "+str(output_actual)

#Testing both beta-reduction strategies by testing a term in which there are duplicate bound variables which represent different objects
#which means the program has to understand the scope of a bound variable and when to stop substituting
def test_scope_of_bound_variables():

    expression = "(%x.x+%x.x)3"
    output_expected = "3+%x.x"

    #Testing call-by-name
    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        output_actual = output_returned[0]

    assert output_expected in output_actual,"test failed because returned = "+str(output_actual)

    #Testing call-by-value
    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        output_actual = output_returned[0]

    assert output_expected in output_actual,"test failed because returned = "+str(output_actual)

#Applications are left-associative, testing this with both beta-reduction strategies by having more than two applications at the same level
def test_order_of_operations():

    expression = "(%x.x*5)3(%y.y+2)"
    output_expected = "15(%y.y+2)"

    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        output_actual = output_returned[0]

    assert output_expected in output_actual,"test failed because returned = "+str(output_actual)

    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        output_actual = output_returned[0]

    assert output_expected in output_actual,"test failed because returned = "+str(output_actual)

#Testing the type returned using beta reduction, by having an abstraction in a lambda term which has an integer input but a boolean output
def test_int_to_bool():

    expression = "(%x.x>4)3"
    output_expected = "False"
    type_expected = "bool"

    #Test call-by-name
    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        output_actual = output_returned[0]
        type_actual = output_returned[2]
        type_actual = type_actual.lower()

    assert output_expected in output_actual and type_expected in type_actual,"test failed because returned = "+str(output_actual)+" with type = "+str(type_actual)

    #Test call-by-value
    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        output_actual = output_returned[0]
        type_actual = output_returned[2]
        type_actual = type_actual.lower()

    assert output_expected in output_actual and type_expected in type_actual,"test failed because returned = "+str(output_actual)+" with type = "+str(type_actual)

#Testing the type-validity section by checking whether a boolean object being manipulated with an integer operation will be picked up as invalid
def test_type_clashing():

    expression = "(%x:bool.x+1)"
    output_expected = "(%x.x+1)"
    type_expected = "false"

    #Test call-by-name
    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        output_actual = output_returned[0]
        type_validity = output_returned[1]
        type_validity = type_validity.lower()

    assert output_expected in output_actual and type_expected in type_validity,"test failed because returned = "+str(output_actual)+" with type = "+str(type_validity)

    #Test call-by-value
    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        output_actual = output_returned[0]
        type_validity = output_returned[1]
        type_validity = type_validity.lower()

    assert output_expected in output_actual and type_expected in type_validity,"test failed because returned = "+str(output_actual)+" with type = "+str(type_validity)

#Testing the type-validity section by checking whether an integer object being manipulated with an integer operation will be picked up as valid
def test_type_valid_clashing():

    expression = "(%x:int.x+1)"
    output_expected = "(%x.x+1)"
    type_expected = "int->int"
    type_validity_expected = "true"

    #Test call-by-name
    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        output_actual = output_returned[0]
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        tupe_actual = type_actual.lower()

    assert output_expected in output_actual and type_expected in type_actual and type_validity_expected in type_validity_actual,"test failed because returned = "+str(output_actual)+" with type validity = "+str(type_validity_actual) + " and type = "+str(type_actual)

    #Test call-by-value
    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        output_actual = output_returned[0]
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        tupe_actual = type_actual.lower()

    assert output_expected in output_actual and type_expected in type_actual and type_validity_expected in type_validity_actual,"test failed because returned = "+str(output_actual)+" with type validity = "+str(type_validity_actual) + " and type = "+str(type_actual)

#Testing the type returned when there are multiple nested functions
def test_type_multiple_function_types():

    expression = "(%x:bool.%y:int.y+1)"
    type_expected = "bool->int->int"
    type_validity_expected = "true"

    #Testing call-by-name
    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        tupe_actual = type_actual.lower()

    assert type_expected in type_actual and type_validity_expected in type_validity_actual,"test failed because type validity = "+str(type_validity_actual) + " and type = "+str(type_actual)

    #Testing call-by-value
    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        tupe_actual = type_actual.lower()

    assert type_expected in type_actual and type_validity_expected in type_validity_actual,"test failed because type validity = "+str(type_validity_actual) + " and type = "+str(type_actual)

#Testing the type-validity section by checking whether the code will pick up a type-clash, the same object being given two conflicting types (int and bool)
def test_variable_type_clashes():

    expression = "(%x:int.x:bool)"
    type_validity_expected = "false"

    #Testing call-by-name
    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()

    assert type_validity_expected in type_validity_actual,"test failed because type validity = "+str(type_validity_actual)

    #Testing call-by-value
    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()

    assert type_validity_expected in type_validity_actual,"test failed because type validity = "+str(type_validity_actual)

#Testing the type inference section with an integer to boolean operation but no explicit typing
def test_type_inference():

    expression = "(%y.y==1)"
    type_validity_expected = "true"
    type_expected = "int->bool"

    #Testing call-by-name
    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        type_actual = type_actual.lower()

    assert type_validity_expected in type_validity_actual and type_expected in type_actual,"test failed because type validity = "+str(type_validity_actual) + " with type = " + str(type_actual)

    #Testing call-by-value
    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        type_actual = type_actual.lower()

    assert type_validity_expected in type_validity_actual and type_expected in type_actual,"test failed because type validity = "+str(type_validity_actual) + " with type = " + str(type_actual)

@pytest.mark.skip
#Testing the type inference section with multiple nested operations and no explicit typing
def test_multi_operation_type_inference():

    expression = "(%x.(x+1)==2)"
    type_validity_expected = "true"
    type_expected = "int->bool"

    #Testing call-by-name
    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        type_actual = type_actual.lower()

    assert type_validity_expected in type_validity_actual and type_expected in type_actual,"test failed because type validity = "+str(type_validity_actual) + " with type = " + str(type_actual)+" when I expected "+str(type_expected)

    #Testing call-by-value
    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        type_actual = type_actual.lower()

    assert type_validity_expected in type_validity_actual and type_expected in type_actual,"test failed because type validity = "+str(type_validity_actual) + " with type = " + str(type_actual)+" when I expected "+str(type_expected)

@pytest.mark.skip
#Testing whether the order of operations for arithmetic operations are followed
def test_order_of_arithmetic():

    expression = "(%x.x^2+x^3)2"
    result_expected = "12"

    #Testing call-by-name
    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        result_actual = output_returned[0]

    assert result_expected == result_actual,"test failed because result = "+str(result_actual)+" when I expected "+str(result_expected)

    #Testing call-by-value
    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        result_actual = output_returned[0]

    assert result_expected == result_actual,"test failed because result = "+str(result_actual)+" when I expected "+str(result_expected)
