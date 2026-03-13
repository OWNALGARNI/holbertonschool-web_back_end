#!/usr/bin/env python3
"""Module for converting key and value to a tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple where:
    - first element is the string k
    - second element is the square of v as a float
    """
    return (k, float(v * v))
