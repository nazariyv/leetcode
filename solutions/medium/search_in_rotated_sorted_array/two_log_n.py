#!/usr/bin/env python
from typing import List

# def search_in_rotated(nums: List[int], target: int) -> int:
# [2,3,1]


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    mid = (l + r) // 2

    while r > l:
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid

        mid = (l + r) // 2

    if l >= 0:
        if nums[l] == target:
            return l

    if r >= 0:
        if nums[r] == target:
            return r

    return -1


def find_inflection_point(nums: List[int]) -> int:
    n = len(nums)
    if n == 0: return -1
    if n == 1: return 0
    if n == 2: return 1 if nums[1] < nums[0] else 0

    lo, hi = 0, n - 1
    mid = (lo + hi) // 2

    while lo + 1 != hi:
        if nums[mid] > nums[hi]:
            lo = mid
        else:
            hi = mid
        mid = (lo + hi) // 2

    return hi if nums[lo] > nums[hi] else lo


def find_in_rotated(nums: List[int], target: int) -> int:
    n = len(nums)
    if n == 0: return -1
    if n == 1: return 0 if nums[0] == target else -1

    rot_idx = find_inflection_point(nums)

    if nums[rot_idx] <= target <= nums[n - 1]:
        r = search(nums[rot_idx:], target)
        if rot_idx == 0:
            return r
        else:
            if r == -1: return -1
            else:
                return r + rot_idx
    elif nums[0] <= target <= nums[rot_idx - 1]:
        return search(nums[:rot_idx], target)

    return -1


if __name__ == '__main__':
    print(find_in_rotated([1,3,0],4))
    ...
