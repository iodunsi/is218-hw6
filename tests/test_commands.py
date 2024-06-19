import pytest 
from app.commands import AddCommand
from app.commands import SubCommand
from app.commands import MultCommand
from app.commands import DivideCommand
from app.commands import MenuCommand


def test_add(capfd):
    """Testing add command"""
    command = AddCommand(1,2)
    command.execute()
    out, err = capfd.readouterr()
    assert out.strip() == "Result: 3"


def test_sub(capfd):
    """Testing subtraction command"""
    command = SubCommand(5,3)
    command.execute()
    out, err = capfd.readouterr()
    assert out.strip() == "Result: 2"

def test_mul(capfd):
    """Testing multiplication command"""
    command = MultCommand(3,4)
    command.execute()
    out,err = capfd.readouterr()
    assert out.strip() == "Result: 12"


def test_div(capfd):
    """Testing division command"""
    command = DivideCommand(10,2)
    command.execute()
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
    
