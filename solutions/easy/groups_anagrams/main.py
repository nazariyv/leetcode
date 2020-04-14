#!/usr/bin/env python
from typing import List
from collections import defaultdict


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print(strs)
        anagrams = defaultdict(list)
        for word in strs:
            print(word)
            anagrams["".join(sorted(word))].append(word)
        return list(anagrams.values())


class Solution:
    def calc_id(self, word: str):
        s = 1
        for char in word:
            s += int.from_bytes(char.encode(), "big") ** 2
        return hash(s)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            _id = self.calc_id(word)
            if _id in anagrams:
                anagrams[_id].add(word)
                continue
            anagrams[_id] = {word}
        return list(anagrams.values())


if __name__ == "__main__":
    s = Solution()
    answer = s.groupAnagrams(['"",""'])
    print("~~~~~~")
    print(answer)
