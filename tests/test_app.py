import pytest
from app import App

def test_app_menu_command(capfd, monkeypatch):
    inputs = iter(['menu'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    app = App()
    app.start()
    
    out, err = capfd.readouterr()
    assert "Available commands:" in out
    assert "- add" in out
    assert "- subtract" in out
    assert "- multiply" in out
    assert "- divide" in out
    assert "- menu" in out

def test_app_add_command(capfd, monkeypatch):
    inputs = iter(['add 10 20'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    app = App()
    app.start()
    
    out, err = capfd.readouterr()
    assert "Result: 30.0" in out

def test_app_subtract_command(capfd, monkeypatch):
    inputs = iter(['subtract 20 10'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    app = App()
    app.start()
    
    out, err = capfd.readouterr()
    assert "Result: 10.0" in out

def test_app_multiply_command(capfd, monkeypatch):
    inputs = iter(['multiply 3 4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    app = App()
    app.start()
    
    out, err = capfd.readouterr()
    assert "Result: 12.0" in out

def test_app_divide_command(capfd, monkeypatch):
    inputs = iter(['divide 8 2'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    app = App()
    app.start()
    
    out, err = capfd.readouterr()
    assert "Result: 4.0" in out

def test_app_divide_by_zero_command(capfd, monkeypatch):
    inputs = iter(['divide 8 0'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    app = App()
    app.start()
    
    out, err = capfd.readouterr()
    assert "Error: Division by zero" in out
