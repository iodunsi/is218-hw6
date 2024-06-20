from app.commands import Command

class MenuCommand(Command):
    '''Menu command'''
 #   def __init__ (self, commands):
  #      self.commands = commands


def execute(self,args):
    print("Avaliable commands:")
    print("- add")
    print("- subtract")
    print("- multiply")
    print("- divide")
    print("- menu")


