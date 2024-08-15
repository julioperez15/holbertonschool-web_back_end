#!/usr/bin/env python3
"""
7. To Kv: provides a function to_kv that
takes a string and an int or float.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string k
    and the second element is the square of v as a float.
    """
    return k, float(v**2)