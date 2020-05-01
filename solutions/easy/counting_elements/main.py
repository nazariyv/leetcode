#!/usr/bin/env python
from typing import List


def count_elements(arr: List[int]) -> int:
    elems = set()
    r = 0
    for a in arr:
        elems.add(a)
    for a in arr:
        if a + 1 in elems:
            r += 1
    return r

if __name__ == '__main__':
    print(count_elements([1,1,2,2]))
