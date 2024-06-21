from app.commands import CommandHandler
from app.plugins.add import AddCommand
from app.plugins.divide import DivideCommand
from app.plugins.multiply import MultCommand
from app.plugins.subtract import SubCommand
from app.plugins.menu import MenuCommand
class App:
    def __init__(self): # Constructor
        '''Config init function'''
        self.command_handler = CommandHandler()

    def start(self):
        '''Start function to initiate'''
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("divide", DivideCommand())
        self.command_handler.register_command("multiply", MultCommand())
        self.command_handler.register_command("subtract", SubCommand())
        self.command_handler.register_command("menu", MenuCommand())
        while True:
            try:
                user_input = input(">>> ").strip()
                if user_input == '':
                    break
                parts = user_input.split()
                command_name = parts[0]
                args = parts[1:]
                self.command_handler.execute_command(command_name, *args)
            except StopIteration:
                break

if __name__ == "__main__":
    app = App()
    app.start()
