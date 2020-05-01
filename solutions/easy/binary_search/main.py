#!/usr/bin/env python
from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        mid = int((l + r) / 2)
        if target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        else:
            return mid
    return nums[l] if target == nums[l] else -1


if __name__ == '__main__':
    print(search([-1,0,3,5,9,12], 9))
