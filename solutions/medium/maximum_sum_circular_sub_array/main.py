#!/usr/bin/env python
from typing import List



class Solution(object):
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kadane(gen: List[int]) -> int:
            ans = cur = 0
            for x in gen:
                cur = max(x, cur + x)
                ans = max(ans, cur)
            return ans
        S = sum(A)
        ans1 = kadane(A)
        ans2 = S + kadane([-1 * A[i] for i in range(len(A))])
        return max(ans1, ans2)



if __name__ == '__main__':
    Solution().maxSubarraySumCircular([1,-2,3,4])
    Solution().maxSubarraySumCircular([-1])
    Solution().maxSubarraySumCircular([-1, -2])
    Solution().maxSubarraySumCircular([-2,1,-3,4,-1,2,1,-5,4])
    Solution().maxSubarraySumCircular([5, -3, 5])
    ...


# [1, -2, 3, 4]
# [1, -1, 3, 7, 8, 6]

# [1, -2, 3, 4, -5, 6, 7,  8]
# [1, -1, 3, 7,  2, 8, 15, 23, 24, 22]  # can only wrap until the start of the subarray
# so here the start is @ 3, so we are only allowed to wrap until (excluding that)

# [1, 5, -1, 4, -20, 3, 4, 5]

# [1, -2, 3, 4, 1, -2, 3]
