#!/usr/bin/env python
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # need to have to conditions to find this. need
        # 1. the element on the left to be smaller, i.e. target > letters[left]  is True
        # 2. the element on the right to be larger, i.e. letters[right] > target is True
        # then return right
        # otherwise return first
        # this is a template II in the binary search templates. i need access to two elements at all times
        l, r = 0, len(letters)

        while l < r:
            mid = l + (r - l) // 2

            if letters[mid] <= target: l = mid + 1  # this will ensure that l is the first element that is larger than target
            else:                     r = mid

        if l == len(letters):
            return letters[0]

        if l >= 1:
            if letters[l - 1] < target and letters[l] > target:
                return letters[l]
        
        return letters[0]


if __name__ == '__main__':
    Solution().nextGreatestLetter(["c","f","j"], "c")
    ...