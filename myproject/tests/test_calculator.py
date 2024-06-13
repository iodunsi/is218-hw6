'''My Calculator Test'''
import pytest
from calculator import add, subtract, multiply, divide
from calculator import Calculator
@pytest.mark.parametrize("num1, num2, outcome",
[
   (2,2,4),
   (1,1,2),
   (0,0,0),
   (-1,-2,-3)

])

def test_addition(num1, num2, outcome):
    '''Test that addition function works '''    
    assert add (num1, num2) == outcome


@pytest.mark.parametrize("num1, num2, outcome",
[
   (2,2,0),
   (1,1,0),
   (0,0,0),
   (-1,-1,0)

])


def test_subtraction(num1, num2, outcome):
    '''Test that - function works '''    
    #assert (subtract(2,2==0))
    assert subtract(num1, num2) == outcome

@pytest.mark.parametrize("num1, num2, outcome",
[
   (2,2,4),
   (1,1,1),
   (0,1,0),
   (-1,-1,1)

])

def test_multi(num1, num2, outcome):
    '''Test that x function works '''    
    assert multiply(num1, num2) == outcome


@pytest.mark.parametrize("num1, num2, outcome",
[
   (2,2,1),
   (1,1,1),
   (0,1,0),
   (-1,-1, 1)

])


def test_div(num1, num2, outcome):
    '''Test that division function works'''    
    if num2 == 0:
        with pytest.raises(ValueError):
            divide(num1, num2)
    else:
        assert divide(num1, num2) == outcome

def calc_hist():
    '''Making sure calc hist. is all good'''
    Calculator.clear_history()
    Calculator.add(2,3)
    Calculator.subtract(5,3)
    assert len(Calculator.get_history()) == 2
    Calculator.clear_history()
    assert len(Calculator.get_history()) == 0


if __name__ == "__main__":
    pytest.main()
 