#!/usr/bin/env python3
"""Module that defines an async comprehension coroutine."""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using an async comprehension
    over async_generator and returns them."""
    return [number async for number in async_generator()]
