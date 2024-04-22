#!/usr/bin/env python3
"""4. Tasks"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times with the specified max_delay.
    Returns the list of all the delays (float values) in ascending order."""
    coros = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*map(lambda x: x, asyncio.as_completed(coros)))
