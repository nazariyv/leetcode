#!/usr/bin/env python
from __future__ import division
from typing import List


class Solution(object):
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - k

        while lo < hi:
            mid = (lo + hi) // 2

            # if x - mid is farther from the target than (mid + k) is from x, then pull lo up
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                # don't need to dedut 1 because hi is ignored. for example lo = 0, hi = 1. what is mid? 0
                hi = mid

        return arr[lo:lo + k]


class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if k == n: return arr
        l, r = 0, n
        idx = -1

        while l < r:
            mid = (l + r) // 2
            if arr[mid] == x: idx = mid; break
            elif arr[mid] < x: r = mid - 1
            else: l = mid + 1

        if idx == -1: return arr[:k]

        if k % 2 == 0:
            return arr[int((idx - k / 2 - 0.5)):int((idx + k / 2))]
        else:
            return arr[int((idx - k / 2)):int((idx + k / 2 + 1))]

        return arr[:k]


if __name__ == '__main__':
    Solution().findClosestElements([1,2,3], 2, -1)
    Solution().findClosestElements([3,4,5], 4, 2)
    Solution().findClosestElements([3,4,5,6,7], 4, 5)
    Solution().findClosestElements([1,1,1,10,10,10], 1 ,9)
    ...