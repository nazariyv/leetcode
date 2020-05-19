#!/usr/bin/env python
from __future__ import division


class Solution:
    def mySqrt(self, x: int) -> int:
        # the sqrt of a number x must lie in 1 < x <= x / 2
        # take for example 4: 1 < x <= 4/2 = 2
        # take for example 9: 1 < x <= 9/2 = 4.5
        # if we take 8, then 1 < x < 4.
        # however, 4 is not the solution, because 4 * 4 = 16
        # and so we halve the problem again
        # the root is now in 2 < x < 4
        # 3 * 3 = 9, close, but not close enough
        # so 2 < x < 3
        # take 2.5, then 2.5 ** 2 = close
        # take 36
        # the answer is in 1 < x <= 18
        # 18 is too large
        # compute 9 * 9
        # too large again


        # the best solution is the Newton's raphson method, that computes the sequence
        # x_{k + 1} = x_k - f(x_k) / f'(x_k)

        # if x < 2:
        #     return x

        # left, right = 2, x // 2

        # while left <= right:
        #     pivot = left + (right - left) // 2
        #     num = pivot * pivot
        #     if num > x:
        #         right = pivot -1
        #     elif num < x:
        #         left = pivot + 1
        #     else:
        #         return pivot

        # return right

        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot

            if num < x:
                left = pivot + 1
            elif num > x:
                right = pivot - 1
            else:
                return pivot



if __name__ == '__main__':
    s = Solution()
    s.mySqrt(8)
    ...