#!/usr/bin/env python
from typing import List


def main(nums: List[int]) -> List[int]:
    out = []
    for i in range(len(nums)):
        product = 0
        for j in range(len(nums)):
            if i != j:
                if nums[j] == 0: product = 0; break
                if product == 0: product = nums[j]; continue
                product *= nums[j]
        out.append(product)
    return out


if __name__ == '__main__':
    t1 = [9, 0, -2]
    r = main(t1)
    print(r)

