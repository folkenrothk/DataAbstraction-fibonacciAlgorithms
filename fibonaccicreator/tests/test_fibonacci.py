"""Add test cases for the functions in the fibonacci module."""

import sympy


from fibonaccicreator import fibonacci


def test_zeroth_fibonacci_empty_tuple():
    """Ensure that the request for the zeroth Fibonacci number returns empty tuple."""
    number = 0
    result = fibonacci.fibonacci_iterativetuple(number)
    assert len(result) == 1
    assert result == (0,)


def test_first_fibonacci_singleton_tuple():
    """Ensure that the request for first Fibonacci number returns same number in a tuple."""
    number = 1
    result = fibonacci.fibonacci_iterativetuple(number)
    assert len(result) == number + 1
    assert result == (
        0,
        1,
    )
    assert sympy.fibonacci(1) == result[-1]


def test_second_fibonacci_tuple():
    """Ensure that the request for the second Fibonacci number returns same number twice in a tuple."""
    number = 2
    result = fibonacci.fibonacci_iterativetuple(number)
    assert len(result) == number + 1
    assert result == (0, 1, 1)
    assert sympy.fibonacci(2) == result[-1]


def test_tenth_fibonacci_tuple():
    """Ensure that the request for the tenth Fibonacci number returns the correct tuple of numbers."""
    number = 10
    result = fibonacci.fibonacci_iterativetuple(number)
    assert len(result) == number + 1
    assert result == (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
    assert sympy.fibonacci(10) == result[-1]


def test_fiftieth_fibonacci_tuple():
    """Ensure that the request for the 50th Fibonacci number is correct according to sympy function."""
    number = 50
    result = fibonacci.fibonacci_iterativetuple(number)
    assert len(result) == number + 1
    assert sympy.fibonacci(50) == result[-1]
