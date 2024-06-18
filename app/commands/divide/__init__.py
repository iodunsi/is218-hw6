from app.commands import Command

class DivideCommand(Command):
    def divide(a, b):
        if b == 0:
            raise ValueError("Division by Zero isn't permitted.")
        return a / b

