#!/usr/bin/env python
from typing import List

def search_in_rotated(nums: List[int], target: int) -> int:
    n = len(nums) - 1
    start, end = 0, n
    while end >= start:
        if end == start:
            if nums[end] == target: return end
        mid = start + (end - start) // 2
        if nums[mid] == target: return mid
        elif nums[start] <= nums[mid]:
            if target >= nums[start] and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target > nums[mid] and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


if __name__ == '__main__':
    search_in_rotated([3,1], 1)
    # search_in_rotated([4,5,6,7,0,1,2], 0)
    # search_in_rotated([4,5,6,7,0,1,2], 4)
    # search_in_rotated([4,5,6,7,0,1,2], -1)
    # search_in_rotated([3, 1], 0)
    # search_in_rotated([3, 1], 4)
    # search_in_rotated([3, 1], 2)
    # search_in_rotated([5,1,3], 1)
    # search_in_rotated([5, 1, 3], 5)
