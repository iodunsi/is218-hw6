'''My Calculator Test'''
import pytest
from calculator import add, subtract, multiply, divide
from calculator import Calculator
@pytest.mark.parametrize("a, b, outcome",
[
   (2,2,4),
   (1,1,2),
   (0,0,0),
   (-1,-2,-3)

])

def test_addition(a, b, outcome):
    '''Test that addition function works '''    
    assert add (a,b) == outcome


@pytest.mark.parametrize("a, b, outcome",
[
   (2,2,0),
   (1,1,0),
   (0,0,0),
   (-1,-1,0)

])


def test_subtraction(a, b, outcome):
    '''Test that - function works '''    
    #assert (subtract(2,2==0))
    assert subtract(a,b) == outcome

@pytest.mark.parametrize("a, b, outcome",
[
   (2,2,4),
   (1,1,1),
   (0,1,0),
   (-1,-1,1)

])

def test_multi(a,b, outcome):
    '''Test that x function works '''    
    assert multiply(a,b) == outcome


@pytest.mark.parametrize("a, b, outcome",
[
   (2,2,1),
   (1,1,1),
   (0,1,0),
   (-1,-1, 1)

])


def test_div(a,b,outcome):
    if b ==0:
        with pytest.raises(ValueError):
            divide(a,b)
    else:
        assert divide(a,b) == outcome
    '''Test that / function works '''    
    assert divide(a,b) == outcome 


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
    '''
    Commenting out old testing logic
    try:
        test_addition()
        print("Addition works")
    except AssertionError:
        print("Something went wrong.")

    try:
        test_subtraction()
        print("Subtraction works")
    except AssertionError:
        print("Something went wrong.")

    try:
        test_multi()
        print("Multiplication works")
    except AssertionError:
        print("Something went wrong.")

    try:
        test_div()
        print("Division works")
    except AssertionError:
        print("Something went wrong.")
    '''
