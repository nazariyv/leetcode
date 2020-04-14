#!/usr/bin/env python
import random
from typing import List
from collections import namedtuple

# constraints
# 1 <= nums.length <= 10^5
max_nums_length = 10 ** 5
# -10^4 <= nums[i] <= 10^4
min_nums = -(10 ** 4)
max_nums = 10 ** 4
# 1 <= k <= nums.length
SMOL = -(10 ** 4 + 1)


reversed_j = lambda j, n: n - 1 - j

# !!! Remove the slicing, it hinders the performance extremely they are all O(k) operations
# ! TODO: challenge: write this code in go concurrently (goroutine for left and goroutine for right)
# ! mistake 1: look at method signatures! do not return a max(nums) i.e. int, when signature says that the output is List[int]
def max_sliding_window(nums: List[int], k: int) -> List[int]:
    if k == 1: return nums
    original_len = len(nums)
    if original_len <= k: return [max(nums)]
    while len(nums) % k != 0: nums.append(SMOL)
    n = len(nums)
    left, right = [], []
    i, j = 0, 1
    while j < n + 1:
        window = nums[k * (i // k):j]
        left.append(max(window))
        i += 1
        if j < n + 1: j += 1
    # ? can I combine the left pass and right pass into a single loop
    # ? does leetcode accept threaded scripts
    i = n - 1
    while i >= 0:
        window = nums[i:(k * ((i // k) + 1))]
        right.append(max(window))
        i -= 1
    windowed_max = []
    i, j = 0, k - 1

    while j < len(left):
        reveresed_i_ix = reversed_j(i, n)
        windowed_max.append(max(left[j], right[reveresed_i_ix]))
        i += 1; j += 1

    len_windowed_max = len(windowed_max)
    while len(windowed_max) > original_len - k + 1: windowed_max.pop()

    return windowed_max


def test_generator():
    length = random.randint(1, max_nums_length)
    while True:
        yield (
            [
                random.randint(
                    min_nums,
                    max_nums
                ) for i in range(length)
            ],
            random.randint(1, length)
        )


if __name__ == '__main__':
    tests = test_generator()
    for i in range(10):
        lst, k = next(tests)
        r = max_sliding_window(lst, k)
        sliding_window_arr = [max(lst[i:i + k]) for i in range(len(lst) - k + 1)]
        assert sliding_window_arr == r, f"expected:{sliding_window_arr},actual:{r}"
    # l = [1,3,-1,-3,5,3,6,7]
    # k = 3
    # actual = max_sliding_window(l, k)
    # expected = [max(l[i:i + k]) for i in range(len(l) - k)]
    # print(f"actual:{actual},expected:{expected}")
    # expected = [3, 3, 5, 5, 6, 7]