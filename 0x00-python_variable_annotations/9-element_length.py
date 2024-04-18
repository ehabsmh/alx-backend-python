#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""
from typing import Sequence, List, Tuple


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    """Returns values with the appropriate types"""
    return [(i, len(i)) for i in lst]
