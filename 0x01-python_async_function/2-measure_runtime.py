#!/usr/bin/env python3
"""2. Measure the runtime"""
from typing import List, Callable, Coroutine, Any

import asyncio
from time import time
wait_n: Callable[[int, int], Coroutine[Any, Any, float]] = __import__(
    '1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time"""
    start_time: float = time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time()
    total_exe: float = (end_time - start_time) / n

    return total_exe
