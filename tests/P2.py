import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../P2')))

from calculator import add, subtract, multiply, divide, calculator


def test_add_integers():
    assert add(2, 3) == 5


def test_add_floats():
    assert add(2.5, 1.2) == pytest.approx(3.7)


def test_subtract_basic():
    assert subtract(10, 4) == 6
    assert subtract(2.5, 1.0) == pytest.approx(1.5)


def test_multiply_basic():
    assert multiply(3, 4) == 12
    assert multiply(2.5, 2) == pytest.approx(5.0)


def test_divide_basic():
    assert divide(7, 2) == pytest.approx(3.5)
    assert divide(9.0, 3.0) == pytest.approx(3.0)


def test_divide_by_zero_returns_error():
    assert divide(5, 0) == "ERROR!"
    assert divide(0, 0) == "ERROR!"


@pytest.mark.parametrize(
    "num1,num2,operator,resultType,expected",
    [
        (5, 2, '+', 'f', 7.0),
        (5, 2, '+', 'i', 7),
        (5.5, 2.2, '+', 'f', pytest.approx(7.7)),
        (5.5, 2.2, '+', 'i', 7),
        (5, 2, '-', 'f', 3.0),
        (5, 2, '-', 'i', 3),
        (5, 2, '*', 'f', 10.0),
        (5, 2, '*', 'i', 10),
        (7, 2, '/', 'f', pytest.approx(3.5)),
        (7, 2, '/', 'i', 3),
        (5.5, 2.2, '/', 'f', pytest.approx(5.5 / 2.2)),
        (5.5, 2.2, '/', 'i', int(5.5 / 2.2)),
        (5, 0, '/', 'f', "ERROR!"),
        (5, 0, '/', 'i', "ERROR!"),
    ],
)
def test_calculator_dispatcher(num1, num2, operator, resultType, expected):
    result = calculator(num1, num2, operator, resultType)

    # If expected is a pytest.approx object use approximate comparison
    if isinstance(expected, type(pytest.approx(0))):
        assert result == expected
        assert isinstance(result, float)
    elif expected == "ERROR!":
        assert result == "ERROR!"
    else:
        # Check types for 'f' vs 'i'
        if resultType == 'f':
            assert isinstance(result, float)
            assert result == pytest.approx(float(expected))
        else:
            assert isinstance(result, int)
            assert result == int(expected)


def test_calculator_types_for_integer_and_float_results():
    # float result type should return float even for integer-valued results
    r = calculator(4, 2, '+', 'f')
    assert isinstance(r, float)

    r2 = calculator(4, 2, '+', 'i')
    assert isinstance(r2, int)
