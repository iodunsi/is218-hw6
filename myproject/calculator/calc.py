from .operations import add, subtract, multiply, divide

class Calc:
    def __init__(self, a, b, operation):
        self.a=a
        self.b=b
        self.operation=operation
    def res(self):
        return self.operation(self.a, self.b)        
    


class Calculator:
    @staticmethod
    def _calc(a,b,operation):
        calc=Calc(a,b,operation)
        return calc.res()
    
    @staticmethod
    def add(a,b):
        return Calculator._calc(a,b, add)

    @staticmethod
    def subtract(a,b):
        return Calculator._calc(a,b, subtract)
    
    @staticmethod
    def multiply(a,b):
        return Calculator._calc(a,b, multiply)
    
    @staticmethod
    def divide(a,b):
        return Calculator._calc(a,b, divide)
    
    @classmethod
    def get_history(cls):
      return cls.history
    
    @classmethod 
    def clear_history(cls):
        cls.history = []

    @classmethod
    def print_history(cls):
        for calc in cls.history:
             print (f'{calc.a} {calc.op} {calc.b} = {calc.res()}'))


