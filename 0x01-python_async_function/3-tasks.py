#!/usr/bin/env python3
"""3. Tasks"""
from typing import List, Callable, Generator, Any
import asyncio
wait_random: Callable[[int], Generator[None, None, Any]] = __import__(
    '0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    return asyncio.Task(wait_random(max_delay))
