import pytest 
from app.commands.add import AddCommand
from app.commands.subtract import SubCommand
from app.commands.multiply import MultCommand
from app.commands.divide import DivideCommand
from app.commands.menu import MenuCommand


def test_add(capfd):
    """Testing add command"""
    command = AddCommand()
    command.execute(1,2)
    out, err = capfd.readouterr()
    assert out.strip() == "Result: 3"


def test_sub(capfd):
    """Testing subtraction command"""
    command = SubCommand()
    command.execute(5,3)
    out, err = capfd.readouterr()
    assert out.strip() == "Result: 2"

def test_mul(capfd):
    """Testing multiplication command"""
    command = MultCommand()
    command.execute(3,4)
    out,err = capfd.readouterr()
    assert out.strip() == "Result: 12"


def test_div(capfd):
    """Testing division command"""
    command = DivideCommand()
    command.execute(10,2)
    out,err = capfd.readouterr()
    assert out.strip() == "Result: 5.0"


def test_menu(capfd):
    """testing menu command"""
    command = MenuCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Available commands:" in out
    assert "- add" in out
    assert "- subtract" in out
    assert "- multiply" in out 
    assert "- divide" in out
    assert "- menu" in out