#!/usr/bin/env python
from typing import List, Callable

from solutions.minions import TestCase as T, TestRunner as TR


Row = int
Col = int

Traverser = Callable[[Row, Col], None]
CrowsNestNavigator = Callable[[Row, Col], bool]


class Solution:
    def number_of_islands(self, treasureMap: List[List[str]]) -> int:
        # loop through each cell, if the cell is 1, then find the boundaries of the island
        # whenever a cell that belongs to a current island is found replacee the value by
        # highest value + 1. This way when you loop through other cells and you fing a non-1
        # cell, then you know the land of that island is accounted for. You can only loop 
        # horizontally and vertically to assign to the island
        # O(n) solution and O(1) space
        m = len(treasureMap)
        n = len(treasureMap[0])
        num_islands = 0

        sail_down:  Traverser = lambda row, col: findTreasure(row + 1, col, treasureMap)
        sail_up:    Traverser = lambda row, col: findTreasure(row - 1, col, treasureMap)
        sail_right: Traverser = lambda row, col: findTreasure(row, col + 1, treasureMap)
        sail_left:  Traverser = lambda row, col: findTreasure(row, col - 1, treasureMap)

        land_down:  CrowsNestNavigator  = lambda row, col: (row + 1) < m  and treasureMap[row + 1][col] == "1"
        land_up:    CrowsNestNavigator  = lambda row, col: (row - 1) > -1 and treasureMap[row - 1][col] == "1"
        land_right: CrowsNestNavigator  = lambda row, col: (col + 1) < n  and treasureMap[row][col + 1] == "1"
        land_left:  CrowsNestNavigator  = lambda row, col: (col - 1) > -1 and treasureMap[row][col - 1] == "1"

        def findTreasure(row: int, col: int, grid: List[List[str]]) -> None:
            nonlocal m, n
            grid[row][col] = "x"
            # for each landpiece, attempt to go left, right, up or down if there is land
            if land_down(row, col):  sail_down(row, col)
            if land_up(row, col):    sail_up(row, col)
            if land_right(row, col): sail_right(row, col)
            if land_left(row, col):  sail_left(row, col)

        for col in range(n):
            for row in range(m):
                if treasureMap[row][col] == "1":
                    findTreasure(row, col, treasureMap)
                    num_islands += 1

        return num_islands


if __name__ == '__main__':
    s = Solution()
    TR(
        (
            T(
                [
                    ["0", "1", "0"],
                    ["1", "1", "1"],
                    ["0", "0", "0"]
                ], expected = 1,
            ),
            T(
                [
                    ["1","0","1","0"],
                    ["0","1","0","1"],
                    ["1","0","1","0"],
                    ["0","1","1","1"]
                ],
                expected = 6
            ),
            T(
                [
                    ["1","1","1","1","0"],
                    ["1","1","0","1","0"],
                    ["1","1","0","0","0"],
                    ["0","0","0","0","0"]
                ],
                expected=1
            )
        ),
        s.number_of_islands
    )()
