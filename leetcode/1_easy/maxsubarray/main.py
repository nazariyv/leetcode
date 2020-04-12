class Solution:
    def maxSubArray(self, nums):
        window_sum, max_sum = nums[0], nums[0]

        for i in range(1, len(nums)):
            window_sum = max(window_sum + nums[i], nums[i])
            max_sum = max(window_sum, max_sum)

        return max_sum


class Solution2:
    # there is an in-built max method!
    @staticmethod
    def max(a, b):
        return a if a > b else b

    def maxSubArray(self, nums):
        """
          Divide and Conquer
        |---------------------------------------------|
        |         [-1,2,6,-4,3,1,5,-5,3,1]            |
        | SOLVE EACH OF THE BELOW PROBLEMS SEPARATELY |
        | [-1,2,6,-4,3]      |  [1,5,-5,3,1]          | the highest sum path will contain the max subarray
        |       6            |       5                | will need to sum left because > 0
        | [-1] [2,6] [-4,3]  |  [1] [5,-5] [3,1]      | if the sum of the left part > 0, we need to add it to subarray
        |        8     -1    |        0      4        |
        |---------------------------------------------|
        -1 8 -1 1 0 4
        1. Divide (sub)array into 2
         if odd length, then first part will have one additional element;
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         note: solve each problem individually, we will have subarrays and their start
         and end indices. If any of the subarrays share the border, then they form
         a new max subarray.
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         note: if len == 3, then split into [.][..]

        {
            (5, 9): [(5, None, 1),  (6, 7, 0), (8, 9, 4)],
            (0, 4): [(0, None, -1), (1, 2, 8), (3, 4, -1)]
        }

        {
            (5, 9): (5, 9, 5),
            (0, 4): (1, 2, 8),
        }

        now check if from the beginning of (5, 9) you can get to (1, 2) without accumulating sum that is <= -8
        if you can then maxSubArray is (1, 9)

        2.
        """
        # [-2,1,-3,4,-1,2,1,-5,4]
        # [0, 3, -1]
        # [-2, 1, 0]
        # [1, 2]
        n = len(nums)
        if n == 1:
            return nums[0]
        run_sum, max_sum, cix = nums[0], nums[0], 1
        while cix != n:
            max_sum = self.max(run_sum, max_sum)
            c = nums[cix]
            if cix == n - 1 and c <= 0 and run_sum > 0:
                return max_sum
            delta = run_sum + c
            if run_sum <= 0 or delta <= 0:
                run_sum, cix = c, cix + 1
                max_sum = self.max(run_sum, max_sum)
                continue
            run_sum, cix = run_sum + c, cix + 1
        return max_sum
