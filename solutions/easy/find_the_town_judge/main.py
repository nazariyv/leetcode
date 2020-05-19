#!/usr/bin/env python
from typing import List, Dict
from collections import defaultdict
from solutions.minions import verbose


class Solution:
    @verbose
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        n = len(trust)
        if len(trust) == 1: return trust[0][1]
        if n < 1 and N == 1: return 1
        if n < 1 and N != 1: return -1

        citizens = N
        trusted_by: Dict[int, int] = defaultdict(int)
        most_trusted = [-1, -1]
        trustees = set()

        for t in trust:
            trustees.add(t[0])
            new_trust = trusted_by[t[1]] + 1
            trusted_by[t[1]] = new_trust

            if new_trust > most_trusted[1]:
                most_trusted[0] = t[1]
                most_trusted[1] = new_trust

        return most_trusted[0] if (most_trusted[1] == N - 1 and most_trusted[0] not in trustees) else -1


if __name__ == '__main__':
    s = Solution()
    s.findJudge(3, [[1, 3], [2, 3]])
    s.findJudge(4, [[1,2],[1,3],[2,1],[2,3],[1,4],[4,3],[4,1]])
    ...
