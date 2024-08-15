#!/usr/bin/env python3
"""
8. Make Multiplier: provides a function make_multiplier
that takes a float multiplier as an argument.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns the product of the float and the multiplier.
    """
    def inner_multiplier(value: float) -> float:
        return value * multiplier

    return inner_multiplier