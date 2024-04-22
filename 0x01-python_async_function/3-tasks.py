#!/usr/bin/env python3
"""3. Tasks"""
from typing import Callable, Generator, Any
import asyncio
wait_random: Callable[[int], Generator[None, None, Any]] = __import__(
    '0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """Takes an integer max_delay and returns a asyncio.Task."""
    return asyncio.create_task(wait_random(max_delay))
