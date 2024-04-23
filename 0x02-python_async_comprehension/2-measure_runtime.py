#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
from typing import List
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime and return it."""
    start_time: float = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time: float = time()

    return end_time - start_time
