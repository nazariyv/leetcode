#!/usr/bin/env python
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i - 1 - j] == nums[i - j]:
                j += 1
                del nums[i - j]

        return len(nums)


if __name__ == '__main__':
    Solution().removeDuplicates([1,1,2])
    Solution().removeDuplicates([1,1,2,2,3,3,3,4,4])
    ...