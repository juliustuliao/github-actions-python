import pytest
from calculator import add, subtract, multiply, divide




def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5
    assert subtract(-5, -5) == 0


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(0, 10) == 0
    assert multiply(-1, 5) == -5


def test_divide():
    assert divide(10, 2) == 5
    assert divide(3, 2) == 1.5

    with pytest.raises(ValueError):
        divide(5, 0)
