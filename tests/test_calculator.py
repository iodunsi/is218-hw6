'''My Calculator Test'''
import pytest
from calculator import divide
#from calculator import Calculator
#@pytest.mark.parametrize("num1, num2, op_name, operation, outcome", [])
def test_operations(num1, num2, op_name, operation, outcome):
    '''Test arithmetic operatios'''
    if op_name == "divide" and num2 == 0:
        with pytest.raises(ValueError):
            divide (num1, num2)
    else:
        assert operation(num1,num2) == outcome
