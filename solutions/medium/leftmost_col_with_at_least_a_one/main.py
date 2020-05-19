#!/usr/bin/env python
from typing import List, Set


class BinaryMatrix:
    __slots__ = ('mat', 'm', 'n', 'api_calls')
    def __init__(self, mat: List[List[int]]):
        self.mat = mat
        self.m = len(self.mat)
        self.n = len(self.mat[0])
        self.api_calls = 0
    def get(self, m: int, n: int) -> int:
        self.api_calls += 1
        if m > self.m or n > self.n:
            return -1
        return self.mat[m][n]
    def dimensions(self) -> List[int]:
        return [self.m, self.n]
    def num_of_calls(self) -> int:
        return self.api_calls

class Solution:
    def leftMostColumnWithOne(self, b: BinaryMatrix) -> int:
        m, n = b.dimensions()

        def find_one_in_col(col: int) -> bool:
            for row_idx in range(m):
                if b.get(row_idx, col):
                    return True
            return False

        leftmost_has_zero = not find_one_in_col(0)
        rightmost_has_one = find_one_in_col(n - 1)

        cols_have_one: Set[int]  = set()
        cols_all_zeros: Set[int] = set()

        if not leftmost_has_zero:
            print(f"{b.num_of_calls()=}")
            return 0
        else:
            cols_all_zeros.add(0)

        if not rightmost_has_one:
            print(f"{b.num_of_calls()=}")
            return -1
        else:
            cols_have_one.add(n - 1)

        if n > 2:
            l_col_idx = 1
            end_idx   = n - 2
        else:
            if leftmost_has_zero and rightmost_has_one:
                return 1
            else:
                return -1

        largest_one_idx = 101
        smallest_zeros_idx = -1

        while (
            l_col_idx <= end_idx
        ):
            if smallest_zeros_idx + 1 == largest_one_idx:
                return largest_one_idx
            mid = l_col_idx + (end_idx - l_col_idx) // 2
            mid_has_one = find_one_in_col(mid)

            if mid_has_one:
                if mid - 1 in cols_all_zeros:
                    return mid
                end_idx = mid
                cols_have_one.add(mid)
                smallest_one_idx = min(largest_one_idx, mid)
            # elif not mid_has_one:
            else:
                l_col_idx = mid
                largest_zero_idx = max(smallest_zeros_idx, mid)
                cols_all_zeros.add(mid)

        return -1


if __name__ == '__main__':
    bm1 = BinaryMatrix([[0,0],[1,1]])
    bm2 = BinaryMatrix([[0, 0], [1, 1], [1, 1]])
    bm3 = BinaryMatrix([[1, 1], [0, 0]])
    bm4 = BinaryMatrix([
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ])
    bm5 = BinaryMatrix([
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1]
    ])
    bm6 = BinaryMatrix([
        [0, 0],
        [0, 1],
    ])
    bm7 = BinaryMatrix([
        [0,0,0,0,1,1],
        [0,0,0,1,1,1],
        [0,0,0,0,1,1],
        [0,0,0,0,1,1],
        [0,0,0,1,1,1],
        [0,0,0,1,1,1]
    ])
    bm8 = BinaryMatrix([
        [0,0,0,1],
        [0,0,1,1],
        [0,1,1,1]
    ])
    bm9 = BinaryMatrix([
        [0,0,0,0,0,0,1,1,1,1,1],
        [0,0,0,0,0,1,1,1,1,1,1],
        [0,0,0,0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,1,1,1,1,1],
        [0,0,0,0,0,1,1,1,1,1,1],
        [0,0,0,0,0,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,1,1],
        [0,0,0,0,1,1,1,1,1,1,1],
        [0,0,1,1,1,1,1,1,1,1,1],
        [0,0,0,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,1,1]
    ])
    s = Solution()
    s.leftMostColumnWithOne(bm9)
    ...