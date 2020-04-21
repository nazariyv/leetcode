#!/usr/bin/env python
from typing import List
from array import array

from solutions.minions import verbose

# ~
# 1 -> -2 | +2 -> 0
# 0 -> -1 | +2 -> 1

@verbose
def num_contiguous(nums: List[int]) -> int:
    if len(nums) < 2: return 0
    zeros, ones = array('B'), array('B')
    max_contiguous = 0
    zeros.append(2 + ~nums[0])  # bitwise not ~, turns every 1 into 0 and every 0 into 1, this is equivalent to -x - 1 
    ones.append(nums[0])

    for num in nums[1:]:
        one_to_append  = ones[-1]  +  num
        zero_to_append = zeros[-1] + ~num + 2
        ones.append(one_to_append)
        zeros.append(zero_to_append)

        if (
            (one_to_append == zero_to_append) and
            (one_to_append > max_contiguous)
        ): max_contiguous = one_to_append

    return 2 * max_contiguous

# class Solution:
#     def findLength(self, nums: List[int]) -> int:
#         n = len(nums)
#         last_ix = n if n % 2 == 0 else n - 1
#         max_running_streak, curr_running_streak = 0, 0
#         for i in range(0, last_ix, 2):
#             if (nums[i] ^ nums[i + 1]): curr_running_streak += 1
#             else:                       curr_running_streak = 0
#             max_running_streak = max(curr_running_streak, max_running_streak)
#         return max_running_streak

#     # sliding window technique
#     def findMaxLength(self, nums: List[int]) -> int:
#         if len(nums) < 2: return 0
#         n1 = self.findLength(nums)
#         n2 = self.findLength(nums[1:])
#         return 2 * max(n1, n2)


if __name__ == '__main__':
    num_contiguous([0,0,0,1,1,1,0])
    num_contiguous([0,0,1,1,1,0,0,0,0,1])
    num_contiguous([0,0,0,0,0])
    num_contiguous([1,1,1,1,1,1,1,1])
    num_contiguous([1,0,1,1])
    num_contiguous([])
    num_contiguous([0])
    num_contiguous([0,0,1,0,0,0,1,1])    # actual = 6
    num_contiguous([0,0,1,0,0,0,0,1,1])  # actual = 4


    #     [0,0,1,0,0,0,1,1]
    #  0s: 1,2,2,3,4,5,5,5
    #  1s: 0,0,1,1,1,1,2,3

    #     [0,0,1,0,0,0,0,1,1]
    #  0s: 1,2,2,3,4,5,6,6,6  # left  to right
    #  1s: 3,3,3,2,2,2,2,2,1  # right to left
    #  1s: 0,0,1,1,1,1,1,2,3  # left  to right

    #     [0,0,1,0,0,0,0,1,1]
    #  0s: 1,2,2,3,4,5,6,6,6  # left  to right
    #  1s: 3,3,3,2,2,2,2,2,1  # right to left
    #  1s: 0,0,1,1,1,1,1,2,3  # left  to right


#   [0,0,1,0,0,0,0,1,1]
#              2 2 2 1
# we can still have a contiguous array with one more 2, for example

#   [0,0,0,1,0,0,0,1,1]
#          3 2 2 2 2 1
# or
#   [0,0,1,1,0,0,0,1,1]
#      4 4 3 2 2 2 2 1
# missing information from the left
# left 1s
# right 1s
#   [0,0,1,1,0,0,0,1,1]
# l [0,0,1,2,2,2,2,3,4]
# r [4,4,4,3,2,2,2,2,1]

