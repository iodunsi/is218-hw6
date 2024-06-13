'''My Calculator Test'''
import pytest
from calculator import add, subtract, multiply, divide
#from calculator import Calculator
@pytest.mark.parametrize("num1, num2, operation, outcome", [])
def test_operations(num1, num2, operation, outcome):
    '''Test arithmetic operatios'''
    assert operation(num1, num2) == outcome 
