#!/usr/bin/env python
from solutions.minions import TestCase as T, TestRunner as TR
from typing import List


# ! CAN BE IMPROVED TO USE CONSTANT SPACE

# T=O(mn), S=O(mn)
def min_path_sum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    supplementary_matrix = [[grid[0][0]]]
    for j in range(1, n):
        supplementary_matrix[0].append(supplementary_matrix[0][-1] + grid[0][j])
    for i in range(1, m):
        supplementary_matrix.append([])
        supplementary_matrix[i].append(supplementary_matrix[i - 1][0] + grid[i][0])
    for j in range(1, m):
        for i in range(1, n):
            supplementary_matrix[j].append(
                grid[j][i] + min(
                    supplementary_matrix[j][i - 1],
                    supplementary_matrix[j - 1][i]
                )
            )
    return supplementary_matrix[m - 1][n - 1]


if __name__ == '__main__':
    TR(
        (
            T(
                case=[
                    [1,3,1],
                    [1,5,1],
                    [4,2,1],
                ], 
                expected=7,
            ),
            T(
                case=[
                    [1, 2, 5, 6],
                    [1, 3, 2, 3],
                    [2, 3, 2, 1],
                    [2, 1, 5, 1],
                ], 
                expected=11,
            ),
            T(
                case=[
                    [1,1,1],
                    [1,1,1],
                    [1,1,1]
                ],
                expected=5,
            ),
            T(
                case=[
                    [1,1,1],
                    [2,2,2],
                ],
                expected=5,
            ),
            T(
                case=[
                    [10,1],
                    [10,2],
                    [1,300],
                    [1,1]
                ],
                expected=23,
            ),
            T(
                case=[
                    [1,4,8,6,2,2,1,7],
                    [4,7,3,1,4,5,5,1],
                    [8,8,2,1,1,8,0,1],
                    [8,9,2,9,8,0,8,9],
                    [5,7,5,7,1,8,5,5],
                    [7,0,9,4,5,6,5,6],
                    [4,9,9,7,9,1,9,0]
                ],
                expected=47,
            ),
        ),
        min_path_sum
    )()
