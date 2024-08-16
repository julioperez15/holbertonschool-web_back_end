#!/usr/bin/env python3
"""
This Module takes wait_n and alters it into a new function.
"""


import asyncio
from typing import List
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    # Creating a list of tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    # Gathering the results
    delays = await asyncio.gather(*tasks)
    # Sorting the results using insertion sort
    for i in range(1, len(delays)):
        element = delays[i]
        j = i - 1
        while j >= 0 and element < delays[j]:
            delays[j + 1] = delays[j]
            j -= 1
        delays[j + 1] = element
    return delays