'''My Calculator Test'''
from calculator import add, subtract, multiply, divide
#assert("Testing this file out")
def test_addition():
    '''Test that addition function works '''    
    assert add (2,2)

def test_subtraction():
    '''Test that - function works '''    
    assert (subtract(2,2==0))

def test_multi():
    '''Test that x function works '''    
    assert multiply(2, 2) == 4

def test_div():
    try:
        result=divide(2,0)
    except ValueError as e:
          assert ("Can't divide by zero")
    '''Test that / function works '''    
    assert (divide(2,2)) 

if __name__ == "__main__":
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

