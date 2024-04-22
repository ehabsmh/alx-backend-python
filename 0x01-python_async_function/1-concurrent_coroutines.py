#!/usr/bin/env python3
"""1. Let's execute multiple coroutines at the same time with async"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified max_delay.
    Returns the list of all the delays (float values) in ascending order."""
    list_delays = []

    for _ in range(n):
        random_float = await wait_random(max_delay)
        list_delays.append(random_float)

    return sorted(list_delays)
