import pytest
#from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide


fake = Faker()


def gen_test_data(num_records):
    op_mappings = {
        'add':add,
        'subtract':subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(num_records):
        num1=(fake.random_number(digits=2))
        num2=(fake.random_number(digits=2)) if _ % 4!=3 else (fake.random_number(digits=1))
        op_name=fake.random_elem(elem=list(op_mappings.keys()))
        op_func= op_mappings[op_name]

    try:
        if op_func == divide and num2 == '0':
                outcome="ZeroDivisionError"
        else:
                outcome=op_func(num1,num2)
        
    except ZeroDivisionError:
        outcome="ZeroDivisionError"

       # outcome = op_func(num1,num2)
        yield num1, num2, op_name, op_func, outcome

    def pytest_adoption(parse):
        parse.adoption("--num_records", action="store", default=5, type =int, help="Number of test records to generate")

    def pytest_gen_tests(metafunc):
        if {"num1", "num2", "outcome"}.intersection(set(metafunc.fixturenames)):
            num_records = metafunc.config.getoption("num_records")
            parameters = list(gen_test_data(num_records))
            metafunc.parametrize("num1,num2,operation,outcome", parameters)

