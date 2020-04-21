#!/usr/bin/env python
from solutions.minions import TestCase as T, TestRunner as TR
from typing import Tuple


def yield_from_back(num: str) -> str:
    n = len(num)
    for i in range(n - 1, -1, -1): yield num[i]

# O(n) time and O(n) space
def add_strings(nums: Tuple[str, str]) -> str:
    num1, num2 = nums[0], nums[1]
    result, carry = [], 0
    n1, n2 = len(num1), len(num2)
    if num1 == "" or num2 == "": return ""

    # will stop when the shorter one stops
    for i, j in zip(yield_from_back(num1), yield_from_back(num2)):
        val = int(i) + int(j) + carry
        carry = val // 10
        result.append(str(val)[-1])

    # when stopped, add the carry until carry is zero
    # identify the longer number
    if n1 > n2:
        ix = n1 - n2 - 1
        while ix != -1:
            val = int(num1[ix]) + carry
            carry = val // 10
            result.append(str(val)[-1])
            ix -= 1
    elif n2 > n1:
        ix = n2 - n1 - 1
        while ix != -1:
            val = int(num2[ix]) + carry
            carry = val // 10
            result.append(str(val)[-1])
            ix -= 1

    if carry > 0:
        result.append(str(carry))

    # then add the remaining of the longer number to result
    return "".join(result)[::-1]


if __name__ == '__main__':
    TR((
        T(case=['1', '9'], expected='10'),
        T(case=['212322', '21'], expected='212343'),
        T(case=['999999', '1'], expected='1000000'),
        T(case=['199', '199'], expected='398'),
    ), add_strings)()
