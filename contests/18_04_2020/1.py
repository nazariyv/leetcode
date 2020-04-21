#!/usr/bin/env python
from solutions.minions import Style
from typing import List

def minStartValue(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        val = nums[0]
        if val < 0:
            return 1 - val
        else:
            return 1

    min_val = nums[0]
    cum_vals = [nums[0]]

    for i in range(1, n):
        cum_val = cum_vals[-1] + nums[i]
        min_val = min(cum_val, min_val)
        cum_vals.append(cum_val)

    if min_val < 0:
        return 1 - min_val
    else:
        return 1


if __name__ == '__main__':
    test_cases = {
        (-2,-3,1,4,): 6,
        (-1,): 2,
        (1,2,3,): 1,
        (0,): 1,
        (2,): 1
    }
    for test, expected in test_cases.items():
        actual = minStartValue(test)
        styler = Style.GREEN if actual == expected else Style.RED
        print(styler(f"actual:{actual},expected:{expected},test:{test}"))
