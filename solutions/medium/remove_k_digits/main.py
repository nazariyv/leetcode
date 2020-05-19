#!/usr/bin/env python
from typing import List

SMOL = -2**31

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack: List[str] = []

        for digit in num:
            while stack and digit < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)

        stack = stack[:-k] if k else stack

        return "".join(stack).lstrip("0") or "0"


class Solution2:
    def removeKdigits(self, num: str, k: int) -> str:
        # "1199"    k=2, remove 99
        # "1919"    k=2, remove 9 at 1 and remove 9 at last index, removing 99
        # "1432219" k=3, 1221, removing 432
        # "1 4  3  2 2 1  9"
        #  7 24 15 8 6 2  9"  
        # need to remove the max number

        n = len(num)

        if k == n: return "0"
        look_after_idx = 0

        num_to_remove = []
        candidate = (SMOL, 1)

        for j in range(k):

            for i in range(look_after_idx, n - k + (j + 1)):  # 7 - 3 + 0 + 1; 7 - 3 + 1 + 1; -> 5, 6, 7

                int_num = (int(num[i]), i)
                if int_num[0] * int_num[1] > candidate[0] * candidate[1]:
                    look_after_idx = i + 1
                    candidate = int_num
                    if int_num[0] == 9: continue

            num_to_remove.append(candidate[0])
            candidate = (SMOL, 1)

        for n in num_to_remove:
            num = num.replace(str(n), "", 1)

        # look for first non-zero element
        first_non_zero = -1

        for ix, nu in enumerate(num):
            if nu != "0":
                first_non_zero = ix
                break

        if first_non_zero != 0:
            return num[first_non_zero:]

        if num == "": return "0"

        # remove leading zeros
        return num


if __name__ == '__main__':
    Solution().removeKdigits("1432219", 3)
    ...
