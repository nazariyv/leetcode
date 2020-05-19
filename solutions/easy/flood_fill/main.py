#!/usr/bin/env python
from typing import List

from solutions.minions import Stack


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        to_sub_color = image[sr][sc]
        if to_sub_color == newColor: return image

        s: Stack = Stack()
        s.push((sr, sc))
        m, n = len(image), len(image[0])

        def helper() -> None:
            try:
                while curr := s.pop():
                    x, y = curr
                    if x + 1 < m  and image[x + 1][y]: s.push((x + 1, y))
                    if x - 1 > -1 and image[x - 1][y]: s.push((x - 1, y))
                    if y + 1 < n  and image[x][y + 1]: s.push((x, y + 1))
                    if y - 1 > -1 and image[x][y - 1]: s.push((x, y - 1))
                    image[x][y] = newColor
            except IndexError:
                pass
        helper()
        return image


if __name__ == '__main__':
    Solution().floodFill([
        [0, 1, 2, 3],
        [0, 1, 3, 4],
        [1, 1, 1, 1]
    ], 1, 1, 21)
    Solution().floodFill([[0,0,0],[0,1,1]], 1, 1, 1)
    ...