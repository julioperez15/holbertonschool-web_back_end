#!/usr/bin/env python3
"""
This module provides a function to measure the runtime of an
asynchronous coroutine.
"""
import time
import asyncio
from concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time and returns the average time per call.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for wait_n.

    Returns:
        float: The average execution time per call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n