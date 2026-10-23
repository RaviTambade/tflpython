from calculator import add, divide
import pytest


def test_add():
    actualResult = add(2, 3)
    expectedResult = 5
    assert actualResult == expectedResult

def test_divide():
    actualResult = divide(10, 2)
    expectedResult = 5
    assert actualResult == expectedResult


def test_divide_by_zero():
    actualResult = divide(10, 0)
    expectedResult = ValueError("Cannot divide by zero")
    assert actualResult == expectedResult
