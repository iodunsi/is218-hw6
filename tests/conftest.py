#import pytest

""" This file is used for config testing"""
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def gen_test_data(num_records):
    """ This is where test data will be generated"""
    op_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(num_records):
        num1 = fake.random_number(digits=2)
        num2 = fake.random_number(digits=2) if _ % 4 != 3 else fake.random_number(digits=1)
        op_name = fake.random_element(elements=list(op_mappings.keys()))
        op_func = op_mappings[op_name]

        try:
            if op_name == 'divide' and num2 == 0:
                outcome = "ValueError"
            else:
                outcome = op_func(num1, num2)
        except ValueError:
            outcome = "ValueError"

        yield num1, num2, op_name, op_func, outcome

def pytest_addoption(parser):
    """adding special cmd line option: --num_records"""
    parser.addoption("--num_records",
                      action="store",
                      default=5,
                      type=int,
                      help="Number of test records to generate"
                      )

def pytest_generate_tests(metafunc):
    """will generate tests at random according to the options set above"""
    if {"num1", "num2", "op_name", "operation", "outcome"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(gen_test_data(num_records))
        metafunc.parametrize("num1,num2, op_name, operation,outcome", parameters)
