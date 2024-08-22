#!/usr/bin/env python3
"""
This module contains an asynchronous generator function
"""


import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates 10 random numbers
    between 0 and 10, with a 1-second delay between each.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
