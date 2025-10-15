import pytest
from src.calc import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(5, 2) == 3

def test_mul():
    assert mul(4, 2.5) == 10

def test_div_normal():
    assert div(10, 4) == 2.5

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div(10, 0)