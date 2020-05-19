#!/usr/bin/env python
from __future__ import division
from collections import defaultdict
from typing import List
from math import gcd as bltin_gcd

from solutions.minions import TestCase as T, TestRunner as TR


def coprime(a: int, b: int) -> bool:
    return bltin_gcd(a, b) == 1


def helper(n: int) -> List[str]:
    res: List[str] = []
    denominator = n

    for i in range(1, n):
        numerator = i

        if i == 1:
            res.append(f"{i}/{denominator}")
            continue

        if coprime(i, denominator):
            res.append(f"{i}/{denominator}")

    return res


def simplifiedFractions(n: int) -> List[str]:
    # if n = 4, then I need to compute the result for each 0, 1, ... n to obtain the result. this can be store in a dict
    res = defaultdict(list)

    for i in range(2, n + 1):
        res[i] = helper(i)
    final_res: List[str] = []

    for v in res.values(): final_res.extend(v)

    return final_res


if __name__ == '__main__':
    TR(
        (
            T(2, ["1/2"]),
            T(1, []),
            T(3, ["1/2", "1/3", "2/3"]),
            T(4, ["1/2", "1/3", "2/3", "1/4", "3/4"]),
            T(5, ["1/2", "1/3", "2/3", "1/4", "3/4", "1/5", "2/5", "3/5", "4/5"]),
            T(6, ["1/2", "1/3", "2/3", "1/4", "3/4", "1/5", "2/5", "3/5", "4/5", "1/6", "5/6"])
        ),
        simplifiedFractions
    )()
    ...