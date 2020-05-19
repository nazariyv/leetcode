#!/usr/bin/env python
from __future__ import division


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2: return True

        f_x =        lambda x: x ** 2 - num
        f_prime_x =  lambda x: 2 * x
        x         = num // 2
        epsilon   = 0.01

        while f_x(x) > epsilon:
            x = x - f_x(x) / f_prime_x(x)

        is_whole_number = x % 1 < epsilon

        return is_whole_number and int(x ** 2) == num


if __name__ == '__main__':
    s = Solution()
    s.isPerfectSquare(14)

