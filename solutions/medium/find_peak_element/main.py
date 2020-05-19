#!/usr/bin/env python
from __future__ import division
from typing import List

SMOL = -2 ** 31

# template 3
# if len(nums) == 0:
#     return -1

# left, right = 0, len(nums) - 1
# while left + 1 < right:
#     mid = (left + right) // 2
#     if nums[mid] == target:
#         return mid
#     elif nums[mid] < target:
#         left = mid
#     else:
#         right = mid

# # Post-processing:
# # End Condition: left + 1 == right
# if nums[left] == target: return left
# if nums[right] == target: return right
# return -1

# this is the template 3 binary search
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]: return mid
            elif nums[mid - 1] > nums[mid] > nums[mid + 1]: r = mid
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]: l = mid + 1
            else:
                if nums[mid + 1] < nums[mid - 1]: r = mid - 1
                else: l = mid + 1
        if nums[l] < nums[r]:
            if r + 1 >= n:
                return r
        return l


class Solution3:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0

        def get(idx: int) -> int:
            if idx == -1 or idx == n: return SMOL
            return nums[idx]

        lo, hi = 0, n
        while lo < hi:
            pivot = (lo + hi) // 2
            if pivot < -1 or pivot > n: return -1

            pivot_val = get(pivot)
            larger_than_left = get(pivot - 1) < pivot_val
            greater_than_right = pivot_val > get(pivot + 1)

            if larger_than_left and greater_than_right: return pivot

            slope_positive = larger_than_left and not greater_than_right
            slope_negative = not larger_than_left and greater_than_right
            # slope_zero = not larger_than_left and not greater_than_right

            if lo + 1 == hi: return - 1

            if slope_positive:
                lo = pivot
            elif slope_negative:
                hi = pivot
            else:
                if pivot < n / 2.0 or pivot >= n - 1:
                    hi = pivot
                else:
                    lo = pivot

        return -1


if __name__ == '__main__':
    Solution().findPeakElement([5,4,1,2,3])
    Solution().findPeakElement([1,2])
    Solution().findPeakElement([1,2,3])
    Solution().findPeakElement([1])
    Solution().findPeakElement([6,5,4,3,4,5,6])
    Solution().findPeakElement([4,5,3,4,5])
    Solution().findPeakElement([-2147483647,-2147483648])
    ...
