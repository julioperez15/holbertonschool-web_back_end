#!/usr/bin/env python3
"""
9. Element Length: calculate the length of elements in an iterable of sequences.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with each sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: List of tuples (sequence, length).
    """
    return [(i, len(i)) for i in lst]