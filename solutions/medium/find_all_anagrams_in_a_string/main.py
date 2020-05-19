#!/usr/bin/env python
from typing import List, Set, Optional
from collections import Counter, deque


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np: return []
        p_count = Counter(p)
        s_count: Counter = Counter()
        output = []
        for i in range(ns):
            s_count[s[i]] += 1
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
            if p_count == s_count: output.append(i - np + 1)
        return output


class MyCounter:
    def __init__(self, count_these: str, should_b: Counter) -> None:
        self.current_count = dict(zip(count_these, [0] * len(count_these)))
        self.should_b = should_b
        self.ans: List[int] = []
        self.curr_ix = 0
        self.queue: deque = deque()
        self.pattern_len = len(count_these)

    def update(self, char: str) -> None:
        if char in self.current_count:
            self.current_count[char] += 1

            increment_ans = True

            for c, v in self.current_count.items():
                if v != self.should_b[c]:
                    increment_ans = False
                    break

            if increment_ans: self.ans.append(self.curr_ix - self.pattern_len + 1)

        self.queue.append(char)

        self.curr_ix += 1

    def pop(self) -> None:
        if not self.queue[0]: return
        char = self.queue.popleft()
        if char in self.current_count:
            self.current_count[char] -= 1

class Solution2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []  # ? can this be handled in the loop?

        should_b = Counter(p)
        p_len = len(p)
        s_len = len(s)
        c = MyCounter(p, should_b)

        for i in range(p_len): c.update(s[i])

        # sliding window
        for i in range(1, s_len - p_len + 1):
            # O(N_p * N_s)
            c.pop()
            c.update(s[i + p_len - 1])

        return c.ans


if __name__ == '__main__':
    Solution().findAnagrams("abab", "ab")
    ...
