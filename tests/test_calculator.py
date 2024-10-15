import pytest
from app.calculator import add, subtract, multiply, divide

def test_add():
    assert add.add(2, 3) == 5

def test_subtract():
    assert subtract.subtract(5, 3) == 2

def test_multiply():
    assert multiply.multiply(2, 3) == 6

def test_divide():
    assert divide.divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide.divide(5, 0)