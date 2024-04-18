#!/usr/bin/env python3
"""8. Complex types - functions"""
from typing import Callable


fn = Callable[[float], float]


def make_multiplier(multiplier: float) -> fn:
    """Takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier."""
    def multiply_float(f: float) -> float:
        return multiplier * f

    return multiply_float
