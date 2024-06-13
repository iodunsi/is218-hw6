'''My Calculator Test'''
import pytest
from calculator import add, subtract, multiply, divide
#from calculator import Calculator
@pytest.mark.parametrize("num1, num2, operation, outcome", [])
def test_operations(num1, num2, operation, outcome):
    '''Test arithmetic operatios'''
    if operation == "divide" and num2 == 0:
        with pytest.raises(ZeroDivisionError):
            divide (num1, num2)
    else:
        assert operation(num1,num2) == outcome
