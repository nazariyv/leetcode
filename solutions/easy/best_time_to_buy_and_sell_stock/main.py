#!/usr/bin/env python
from solutions.minions import TestRunner as TR, TestCase as T
from collections import deque
from typing import List
import logging
log = logging.getLogger("best_time_to_buy_and_sell_stock")


# T=O(n),S=O(1)
def main(prices: List[int]) -> int:
    n = len(prices)
    max_profit = 0
    min_so_far = prices[0]
    for i in range(1, n):
        min_so_far = min(min_so_far, prices[i])
        max_profit = max(max_profit, prices[i] - min_so_far)
    return max_profit


# LARGE = 2 ** 32 - 1
# SMALL = -(2 ** 32)
# def find_max_so_far(max_so_far, prices, ix):
#     if max_so_far[0] < prices[ix]:
#         max_so_far = prices[ix], ix
#     return max_so_far
# def find_min_so_far(min_so_far, prices, ix):
#     if min_so_far[0] > prices[ix]:
#         min_so_far = prices[ix], ix
#     return min_so_far

# def main(prices: List[int]) -> int:
#     n = len(prices)
#     if n < 2: return 0
#     min_so_far = [LARGE, 0]
#     max_so_far = [SMALL, n - 1]
#     max_profit = 0
#     for i in range(0, n):
#         max_so_far = find_max_so_far(max_so_far, prices, n - i - 1)
#         min_so_far = find_min_so_far(min_so_far, prices, i)
#         if max_so_far[1] > min_so_far[1]:
#             max_profit = max(max_profit, max_so_far[0] - min_so_far[0])
#     return max_profit

# def main(prices: List[int]) -> int:
#     n = len(prices)
#     if n < 2: return 0
#     min_left = [prices[0]]
#     max_right = [prices[n - 1]]
#     max_profit = 0
#     for i in range(1, n):
#         min_left.append(min(prices[i], min_left[-1]))
#         max_right.append(max(prices[n - 1 - i], max_right[-1]))
#     for i in range(0, n):
#         max_profit = max(max_profit, max_right[n - 1 - i] - min_left[i])
#     return max_profit

# very slow
# def main(prices: List[int]) -> int:
#     n = len(prices)
#     if n < 2: return 0
#     mins_left = [prices[0]]
#     max_right = deque([prices[-1]])
#     for i in range(1, n):
#         price = prices[i]
#         if mins_left and mins_left[-1] > price:
#             mins_left.append(price)
#         else:
#             mins_left.append(mins_left[-1])
#     for i in range(n - 2, -1, -1):
#         price =  prices[i]
#         if max_right and max_right[0] < price:
#             max_right.appendleft(price)
#         else:
#             max_right.appendleft(max_right[0])
#     max_profit = 0
#     for i in range(0, n):
#         max_profit = max(max_profit, max_right[i] - mins_left[i])
#     return max_profit


if __name__ == '__main__':
    TR(
        (
            T(case=[7,1,2,3,4,5,6], expected=5),
            T([7,6,5,4], 0),
            T([1,2,3,4,10], 9),
            T([2,1,2,1,0,0,1], 1)
        ),
        main
    )()
