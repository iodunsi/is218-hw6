from app.commands import CommandHandler
from app.commands.add import AddCommand 
from app.commands.divide import DivideCommand
from app.commands.multiply import MultCommand
from app.commands.subtract import SubCommand 
from app.commands.menu import MenuCommand

class App:
    def __init__(self): # Constructor
        '''Config init function'''
        self.command_handler = CommandHandler()


    def start(self):
        '''Start function to initiate'''
        # Register commands here
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command("muliply", MultCommand())
        self.command_handler.register_command("subtract", SubCommand())
        self.command_handler.register_command("menu", MenuCommand())

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())


