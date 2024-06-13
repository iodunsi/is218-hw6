import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator  # Assuming Calculator is defined as shown previously

class OperationCommand:
    def __init__(self, calculator, operation_name, num1, num2):
        self.calculator = calculator
        self.operation_name = operation_name
        self.num1 = num1
        self.num2 = num2

    def execute(self):
        # Retrieve the operation method from the Calculator class using getattr
        operation_method = getattr(self.calculator, self.operation_name, None)
        if operation_method:
            return operation_method(self.num1, self.num2)
        else:
            raise ValueError(f"Unknown operation: {self.operation_name}")

def calculate_and_print(num1, num2, operation_name):
    try:
        a_decimal, b_decimal = map(Decimal, [num1, num2])
        command = OperationCommand(Calculator, operation_name, a_decimal, b_decimal)
        result = command.execute()
        print(f"The result of {num1} {operation_name} {num2} is equal to {result}")
    except InvalidOperation:
        print(f"Invalid number input: {num1} or {num2} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, num1, num2, operation_name = sys.argv
    calculate_and_print(num1, num2, operation_name)

if __name__ == '__main__':
    main()