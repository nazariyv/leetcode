#!/usr/bin/env python
from typing import List

# * 
class Solution:
    def findLength(self, nums: List[int]) -> int:
        n = len(nums)
        last_ix = n if n % 2 == 0 else n - 1
        max_running_streak, curr_running_streak = 0, 0
        for i in range(0, last_ix, 2):
            if (nums[i] ^ nums[i + 1]): curr_running_streak += 1
            else:                       curr_running_streak = 0
            max_running_streak = max(curr_running_streak, max_running_streak)
        return max_running_streak

    # sliding window technique
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        n1 = self.findLength(nums)
        n2 = self.findLength(nums[1:])
        return 2 * max(n1, n2)


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxLength([0,1,1,1,0,0,1,1,0]))


# dynamic programming
# [0,0,1,1,1,0]
# [0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1]
# any invariants?
# the subarray's 

1 & 0 == 0
1 & 1 == 1
0 & 0 == 1

000111
1 0 1 -> 0 & 1 -> 0
0011
1  1 -> 1

000111
0 1 0
 1 0 -> 1

0011
0  0 -> 0

can use AND for odd len and XOR for even to get output 0 if subarray
or
can use AND for even len and XOR for odd to get output 1 if subarray

are these unique or can they produce other undesirable output?


000011 -> is also 1