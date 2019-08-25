import pytest
import sys
sys.path.append("..")
from LambdaCalculus import unit_t_interface

@pytest.mark.skip
def test_call_by_value():

    expression = "(%x.%y.y)((%z.zz)(%z.zz))"
    output_expected = "cannot be found"

    output_returned = unit_t_interface(expression,"v")

    output_actual = output_returned

    assert output_expected in output_actual,"test failed because returned = "+str(output_actual)

@pytest.mark.skip
def test_call_by_name():

    expression = "(%x.%y.y)((%z.zz)(%z.zz))"
    output_expected = "(%y.y)"

    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        output_actual = output_returned[0]

    assert output_expected in output_actual,"test failed because returned = "+str(output_actual)

@pytest.mark.skip
def test_multi_input():

    expression = "(%b.b+(%a.a+b)3)4"
    output_expected = "11"

    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        output_actual = output_returned[0]

    assert output_expected in output_actual,"test failed because returned = "+str(output_actual)

    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        output_actual = output_returned[0]

    assert output_expected in output_actual,"test failed because returned = "+str(output_actual)

@pytest.mark.skip
def test_scope_of_bound_variables():

    expression = "(%x.x+%x.x)3"
    output_expected = "3+%x.x"

    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        output_actual = output_returned[0]

    assert output_expected in output_actual,"test failed because returned = "+str(output_actual)

    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        output_actual = output_returned[0]

    assert output_expected in output_actual,"test failed because returned = "+str(output_actual)

@pytest.mark.skip
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

@pytest.mark.skip
def test_int_to_bool():

    expression = "(%x.x>4)3"
    output_expected = "False"
    type_expected = "bool"

    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        output_actual = output_returned[0]
        type_actual = output_returned[2]
        type_actual = type_actual.lower()

    assert output_expected in output_actual and type_expected in type_actual,"test failed because returned = "+str(output_actual)+" with type = "+str(type_actual)

    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        output_actual = output_returned[0]
        type_actual = output_returned[2]
        type_actual = type_actual.lower()

    assert output_expected in output_actual and type_expected in type_actual,"test failed because returned = "+str(output_actual)+" with type = "+str(type_actual)

@pytest.mark.skip
def test_type_clashing():

    expression = "(%x:bool.x+1)"
    output_expected = "(%x.x+1)"
    type_expected = "false"

    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        output_actual = output_returned[0]
        type_validity = output_returned[1]
        type_validity = type_validity.lower()

    assert output_expected in output_actual and type_expected in type_validity,"test failed because returned = "+str(output_actual)+" with type = "+str(type_validity)

    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        output_actual = output_returned[0]
        type_validity = output_returned[1]
        type_validity = type_validity.lower()

    assert output_expected in output_actual and type_expected in type_validity,"test failed because returned = "+str(output_actual)+" with type = "+str(type_validity)

@pytest.mark.skip
def test_type_valid_clashing():

    expression = "(%x:int.x+1)"
    output_expected = "(%x.x+1)"
    type_expected = "int->int"
    type_validity_expected = "true"

    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        output_actual = output_returned[0]
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        tupe_actual = type_actual.lower()

    assert output_expected in output_actual and type_expected in type_actual and type_validity_expected in type_validity_actual,"test failed because returned = "+str(output_actual)+" with type validity = "+str(type_validity_actual) + " and type = "+str(type_actual)

    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        output_actual = output_returned[0]
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        tupe_actual = type_actual.lower()

    assert output_expected in output_actual and type_expected in type_actual and type_validity_expected in type_validity_actual,"test failed because returned = "+str(output_actual)+" with type validity = "+str(type_validity_actual) + " and type = "+str(type_actual)

@pytest.mark.skip
def test_type_multiple_function_types():

    expression = "(%x:bool.%y:int.y+1)"
    type_expected = "bool->int->int"
    type_validity_expected = "true"

    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        tupe_actual = type_actual.lower()

    assert type_expected in type_actual and type_validity_expected in type_validity_actual,"test failed because type validity = "+str(type_validity_actual) + " and type = "+str(type_actual)

    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        tupe_actual = type_actual.lower()

    assert type_expected in type_actual and type_validity_expected in type_validity_actual,"test failed because type validity = "+str(type_validity_actual) + " and type = "+str(type_actual)

@pytest.mark.skip
def test_variable_type_clashes():

    expression = "(%x:int.x:bool)"
    type_validity_expected = "false"

    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()

    assert type_validity_expected in type_validity_actual,"test failed because type validity = "+str(type_validity_actual)

    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()

    assert type_validity_expected in type_validity_actual,"test failed because type validity = "+str(type_validity_actual)

@pytest.mark.skip
def test_type_inference():

    expression = "(%y.y==1)"
    type_validity_expected = "true"
    type_expected = "int->bool"

    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        type_actual = type_actual.lower()

    assert type_validity_expected in type_validity_actual and type_expected in type_actual,"test failed because type validity = "+str(type_validity_actual) + " with type = " + str(type_actual)

    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        type_actual = type_actual.lower()

    assert type_validity_expected in type_validity_actual and type_expected in type_actual,"test failed because type validity = "+str(type_validity_actual) + " with type = " + str(type_actual)

def test_multi_operation_type_inference():

    expression = "(%x.(x+1)==2)"
    type_validity_expected = "true"
    type_expected = "int->bool"

    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        type_actual = type_actual.lower()

    assert type_validity_expected in type_validity_actual and type_expected in type_actual,"test failed because type validity = "+str(type_validity_actual) + " with type = " + str(type_actual)+" when I expected "+str(type_expected)

    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        type_validity_actual = output_returned[1]
        type_validity_actual = type_validity_actual.lower()
        type_actual = output_returned[2]
        type_actual = type_actual.lower()

    assert type_validity_expected in type_validity_actual and type_expected in type_actual,"test failed because type validity = "+str(type_validity_actual) + " with type = " + str(type_actual)+" when I expected "+str(type_expected)

def test_order_of_arithmetic():

    expression = "(%x.x^2+x^3)2"
    result_expected = "12"

    output_returned = unit_t_interface(expression,"n")

    if len(output_returned) > 2:
        result_actual = output_returned[0]

    assert result_expected == result_actual,"test failed because result = "+str(result_actual)+" when I expected "+str(result_expected)

    output_returned = unit_t_interface(expression,"v")

    if len(output_returned) > 2:
        result_actual = output_returned[0]

    assert result_expected == result_actual,"test failed because result = "+str(result_actual)+" when I expected "+str(result_expected)
