from typing import List, TypeVar
from random import random

from solutions.minions import Stack

T = TypeVar('T')


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        s: Stack = Stack()
        m, n = len(grid), len(grid[0])
        if m == n == 1: return 4
        mn = m * n
        perimeter = 0
        r = (int(random() * m), int(random() * n))
        looked_at = set([r])
        while grid[r[0]][r[1]] != 1 and len(looked_at) != mn:
            while r in looked_at: r = (int(random() * m), int(random() * n))
            looked_at.add(r)
        s.push(r)
        try:
            while curr := s.pop():
                x, y = curr
                if grid[x][y] == -1: continue # !
                grid[x][y] = -1
                if x == 0:
                    perimeter += 1
                if x == m - 1:
                    perimeter += 1
                if y == 0:
                    perimeter += 1
                if y == n - 1:
                    perimeter += 1
                if x - 1 > -1:
                    loc = grid[x - 1][y]
                    if loc == 0: perimeter += 1
                    elif loc == 1: s.push((x - 1, y))
                if x + 1 < m:
                    loc = grid[x + 1][y]
                    if loc == 0: perimeter += 1
                    elif loc == 1: s.push((x + 1, y))
                if y - 1 > -1:
                    loc = grid[x][y - 1]
                    if loc == 0: perimeter += 1
                    elif loc == 1:s.push((x, y - 1))
                if y + 1 < n:
                    loc = grid[x][y + 1]
                    if loc == 0: perimeter += 1
                    elif loc == 1: s.push((x, y + 1))
        except IndexError: pass

        return perimeter
