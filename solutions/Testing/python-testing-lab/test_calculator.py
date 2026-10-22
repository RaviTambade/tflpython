from calculator import add, divide
import pytest


def test_add_two_numbers():
    assert add(10, 20) == 30


def test_divide_two_numbers():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-2, 2, 0),
        (100, 200, 300),
    ],
)
def test_addition_cases(a, b, expected):
    assert add(a, b) == expected

