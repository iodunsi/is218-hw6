from app.commands import Command

class AddCommand(Command):
    '''Adding command'''
   # def __init__(self):
    #    pass

    def execute(self, *args):
        a,b=map(float,args)
        result = a + b
        print(f"Result: {result}")