from app.commands import Command

class MenuCommand(Command):
    '''Menu command'''
    def __init__ (self, commands):
        self.commands = commands


def execute(self):
    '''Execution function for commands'''
    print("Avaliable commands:")
    for command in self.commands:
        print(f"- {command}")