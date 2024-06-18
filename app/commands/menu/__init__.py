from app.commands import Command

class MenuCommand(Command):
    def __init__ (self, commands):
        self.commands = commands


def execute(self):
    print("Avaliable commands:")
    for command in self.commands:
        print(f"- {command}")