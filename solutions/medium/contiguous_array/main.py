#!/usr/bin/env python
from solutions.minions import TestCase as T, TestRunner as TR
from collections import defaultdict
from typing import List

from solutions.minions import verbose
val_mapper = {1: 1, 0: -1}

@verbose
def num_contiguous(nums: List[int]) -> int:
    val_idx_map  = defaultdict(list)
    curr, prev, r = 0, 0, 0
    for idx, n in enumerate(nums):
        curr = val_mapper[n] + prev
        if curr == 0: r = max(r, idx + 1)
        val_idx_map[curr].append(idx)
        r = max(r, val_idx_map[curr][-1] - val_idx_map[curr][0])
        prev = curr
    return r


if __name__ == '__main__':
    TR((
        T([0,0,0,1,1,1,0], 6),
        T([0,0,1,1,1,0,0,0,0,1], 8),
        T([0,0,0,0,0], 0),
        T([1,1,1,1,1,1,1,1], 0),
        T([1,0,1,1], 2),
        T([], 0),
        T([0], 0),
        T([0,0,1,0,0,0,1,1], 6),   # actual = 6
        T([0,0,1,0,0,0,0,1,1], 4),  # actual = 4
    ), num_contiguous)()


# let 0 map to -1 and 1 map to 1, then
# [0,  0, 1, 0, 0, 0, 1,  1] would become
# [-1,-2,-1,-2,-3,-4, -3, -2]

# [0,   0,  1,   0,  0,  0,  1,  1]
# [-1, -2, -1,  -2, -3, -4, -3, -2]

