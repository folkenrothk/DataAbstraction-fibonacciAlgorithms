"""Compute values in the Fibonacci sequence using different approaches."""

# TODO: Import all of the needed type annotations


def fibonacci_recursivelist(number: int) -> List[int]:
    """Start with 0 and compute up to and include the number-th Fibonacci number using recursion and a list."""
    # Reference:
    # https://stackoverflow.com/questions/33325683/python-creating-a-list-of-the-first-n-fibonacci-numbers
    # TODO: Base case: return [0, 1] when number is either 0 or 1
    # TODO: Recursive case: perform the computation for number - 1 and
    # then append to the list the two previous computations added together
    # TODO: Finally, return the current version of the list.


def fibonacci_recursivetuple(number: int) -> Tuple[int, ...]:
    """Start with 0 and compute up to and include the number-th Fibonacci number using recursion and a list."""
    # Reference:
    # https://stackoverflow.com/questions/33325683/python-creating-a-list-of-the-first-n-fibonacci-numbers
    # Note that the reference describes the computation for lists and not tuples
    # TODO: Base case: return [0, 1] when number is either 0 or 1
    # TODO: Recursive case: perform the computation for number - 1 and
    # then "append" to the tuple the two previous computations added together,
    # bearing in mind that the use of += will create a new tuple.
    # TODO: Finally, return the current version of the tuple.


def fibonacci_iterativetuple(number: int) -> Tuple[int, ...]:
    """Start with 0 and compute up to and including the number-th Fibonacci number using iteration and a tuple."""
    # TODO: create an empty tuple that will ultimately contain the results
    # TODO: set the initial conditions of the sequence
    # Note: start at 0 and 1, not at 1 and 1 like in the course slides
    # Note: different start is to ensure consistency with this article:
    # https://realpython.com/fibonacci-sequence-python/
    # TODO: iterate from zero to the (number)th number
    # --> TODO: store the value of a in the tuple
    # --> TODO: move to the next value such that:
    # --> TODO: a gets the current value of b
    # --> TODO: b gets the current value of a + b
    # TODO: return the final tuple that contains the fibonacci numbers


def fibonacci_iterativelist(number: int) -> List[int]:
    """Start with 0 and compute up to and including the number-th Fibonacci number using a list."""
    # TODO: create an empty list that will ultimately contain the results
    # TODO: set the initial conditions of the sequence
    # Note: start at 0 and 1, not at 1 and 1 like in the course slides
    # Note: different start is to ensure consistency with this article:
    # https://realpython.com/fibonacci-sequence-python/
    # TODO: set the initial conditions of the sequence
    # TODO: iterate from zero to the (number)th number
    # --> TODO: store the value of a in the list
    # --> TODO: move to the next value such that:
    # --> TODO: a gets the current value of b
    # --> TODO: b gets the current value of a + b
    # TODO: return the final tuple that contains the fibonacci numbers
