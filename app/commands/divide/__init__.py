from app.commands import Command

class DivideCommand(Command):
    '''Dividing command'''
  #  def __init__(self):
 #        pass

def execute(self, args):
        a,b = map(float,args)
        if b == 0:
            print("Error: Division by zero")
        else:
            result = a / b
            print(f"Result: {result}")