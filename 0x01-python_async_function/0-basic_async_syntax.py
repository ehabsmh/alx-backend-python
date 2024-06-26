#!/usr/bin/env python3
"""0. The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it."""
    random_float: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
