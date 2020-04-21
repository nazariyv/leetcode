#!/usr/bin/env python
from solutions.minions import TestRunner as TR, TestCase as T, iterable_comparator
from typing import List


# division is just repeated subtraction. T=O(num/divisor)
def repeated_subtraction(num: int, divisor: int):
    steps = 0
    while num > 0: num -= divisor; steps += 1
    return steps

# S=O(n), T=O(n)
def product_except_self(nums: List[int]) -> List[int]:
    total_product, out = None, []
    num_of_zeros = 0

    for num in nums:
        if num == 0: num_of_zeros += 1; continue
        if total_product is None: total_product = 1
        total_product *= num

    if num_of_zeros > 1: return [0] * len(nums)

    for num in nums:
        if num_of_zeros == 1 and num != 0: out.append(0)
        elif num == 1 or num == 0:         out.append(total_product)
        else:                              out.append(repeated_subtraction(total_product, num))

    return out


if __name__ == '__main__':
    TR(
        (
            T([1,2,3,4],       [24, 12, 8, 6]),
            T([1],             [1]),
            T([5,10],          [10, 5]),
            T([1, 0],          [0, 1]),
            T([0,1,2],         [2,0,0]),
            T([0, 0],          [0, 0]),
            T([0, 1, 0],       [0, 0, 0]),
            T([1,1,1,0],       [0,0,0,1]),
            T([0,0,0,1,0,0],   [0,0,0,0,0,0]),
            T([1, -1],         [-1, 1]),
            T([1, -2, -10, 2], [40, -20, -4, 20])
        ),
        product_except_self,
        iterable_comparator,
    )()
