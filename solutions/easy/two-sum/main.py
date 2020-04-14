#!/usr/bin/env python
from typing import List

def main(nums: List[int], target: int) -> List[int]:
    if len(nums) < 2: raise Exception("invalid input")
    remainder = dict()
    for ix, num in enumerate(nums):
        if num in remainder: return (remainder[num], ix)
        need = target - num
        if need not in remainder: remainder[need] = ix
        # < 0:  overshot
        # ! mistake 1: == 0: contradiction. only one solution should be available
        # ! consider: [0, 4, 3, 0] and target of 0
        # ! mistake 2: assuming that target > 0


if __name__ == '__main__':
    print(main([-1, -2, -3, -4, -5], -8))
