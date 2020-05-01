#!/usr/bin/env python
from typing import List


map_ix = lambda inflxn, n: n - inflxn - 1

def find_inflection_point(start_ix: int, end_ix: int, nums: List[int]):
    prev = nums[start_ix]
    for i in range(start_ix + 1, end_ix + 1):
        if nums[i] < prev:
            return i

# def search(nums: List[int], target: int):
#     n = len(nums)
#     inflection_point = None
#     mid = n // 2

#     while True:
#         if target < nums[mid]:
#             new_mid = mid // 2
#             if nums[new_mid] > nums[mid]:
#                 inflection_point = find_inflection_point(new_mid, mid, nums)
#                 mid = map_ix(n) // 2
#         elif target > nums[mid]:
#             new_mid = mid + mid // 2
#             if nums[new_mid] < nums[mid]:
#                 inflection_point = find_inflection_point(mid, new_mid, nums)
#                 mid = map_ix(n) // 2
#         else:
#             return mid

def binary_find(nums: List[int], target: int) -> int:
    def search(l: int, r: int):
        if l == r:
            if nums[l] == target:
                return l
            else:
                return -1
        mid = int((l + r) / 2)
        if nums[mid] == target: 
            return mid
        elif nums[mid] < target:
            return search(mid + 1, r)
        else:
            return search(mid - 1, l)
    return search(0, len(nums) - 1)


if __name__ == '__main__':
    print(binary_find([1,2,3,4,5,6], 6))

# [7,1,4,5,6]
# [10,20,5,6,7]
