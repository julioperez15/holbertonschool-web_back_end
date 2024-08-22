#!/usr/bin/env python3
"""
Helper function for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate start and end indices for pagination.

    Args:
        page (int): Page number.
        page_size (int): Items per page.

    Returns:
        tuple: Start and end indices.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
