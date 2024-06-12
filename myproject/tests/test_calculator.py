'''My Calculator Test'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''    
    print (add(2,2)) #== 4)

def test_subtraction():
    '''Test that - function works '''    
    print (subtract(2,2)) #== 0

def test_multi():
    '''Test that x function works '''    
    print (multiply(2,2)) #== 4

def test_div():
    try:
        result=divide(2,0)
    except ValueError as e:
          print ("Can't divide by zero")
    '''Test that / function works '''    
    print (divide(2,2)) 

