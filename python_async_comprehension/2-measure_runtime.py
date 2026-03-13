#!/usr/bin/env python3
"""Module that measures runtime for running async_comprehension in parallel."""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times in parallel and returns total runtime."""
    start_time: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time: float = time.perf_counter()
    return end_time - start_time
