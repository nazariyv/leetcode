#!/usr/bin/env python
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l, r = 0, len(nums) - 1
        out = [-1, -1]

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                out[0], out[1] = mid, mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        # right + 1 == left.
        if out[0] == -1: return out

        delta = 1
        while out[0] - delta > 0 and nums[out[0] - delta] == target:
            delta += 1
        out[0] = out[0] - delta + 1

        delta = 1
        while out[1] + delta < len(nums) and nums[out[1] + delta] == target:
            delta += 1
        out[1] = out[1] + delta - 1

        return out


if __name__ == '__main__':
    Solution().searchRange([1,2,2,3], 2)
    Solution().searchRange([1], 1)
    Solution().searchRange([1,2,2,2,2,2,3], 3)
    Solution().searchRange([2,2,3,3,4,4,4], 4)
    Solution().searchRange([1,1,2], 1)
    ...
