#!/usr/bin/env python
import logging
from solutions.minions import Style
from typing import List

log = logging.getLogger("sss")


# !
def fib():
    prev, next_ = 0, 1
    while True:
        yield prev
        prev, next_ = next_, prev + next_


def find_sum(fib_nums: List[int], k: int):
    largest = fib_nums[-1]  # TODO: potential index error
    last_ix = -1
    remaining_sum = k
    operations = 0
    while remaining_sum != 0:
        if largest > remaining_sum:
            last_ix -= 1
            largest = fib_nums[last_ix]
            continue
        elif largest == remaining_sum:
            operations += 1
            remaining_sum = 0
            return operations
        elif remaining_sum % largest == 0:
            operations += remaining_sum // largest
            remaining_sum = 0
            return operations
        else:
            operations += 1
            remaining_sum -= largest
            last_ix -= 1
            largest = fib_nums[last_ix]
            continue
    return operations


def findMinFibonacciNumbers(k: int) -> int:
    fib_gen = fib()
    fib_nums = [next(fib_gen)]
    while fib_nums[-1] < k: fib_nums.append(next(fib_gen))
    min_nums = find_sum(fib_nums, k)
    return min_nums


if __name__ == '__main__':
    test_cases = {
        7: 2,
        10: 2,
        19: 3,
        610: 1,
        145: 2,
        1: 1,
        96151855463018422468774569: 2,
    }
    
    for test, expected in test_cases.items():
        actual = findMinFibonacciNumbers(test)
        styler = Style.GREEN if actual == expected else Style.RED
        log.info(styler(f"actual:{actual},expected:{expected},test:{test}"))
