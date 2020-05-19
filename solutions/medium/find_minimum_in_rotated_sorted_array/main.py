#!/usr/bin/env python
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        l, r = 0, n - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid] < nums[l] or nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r] or nums[mid] > nums[l]:
                l = mid
            else:
                breakpoint()
                raise Exception('never')

        return nums[l]
        # if rotated, then every element after the rot
        # index is smaller than every element before the
        # rot idx


if __name__ == '__main__':
    Solution().findMin([4,5,6,9,10,1,2])
    Solution().findMin([3,4,5,1,2])
    Solution().findMin([2,3,4,5,1])
    ...