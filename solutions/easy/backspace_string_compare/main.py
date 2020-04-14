#!/usr/bin/env python
from array import array
from typing import Iterable
import collections
BACKSPACE = 35

# def clean_word(word):
#     word = word[::-1];  # O(n)
#     return re.sub(r"#.", "", word)  # O(2^m + n), m substitutions, n length

# def clean_word_2(word: Iterable[int]):
#     how_many_to_delete = 0
#     lw = len(word)

#     # to loop through each char is O(n) operation. To pop is another O(n) at worst, so this part here is O(n ** 2)
#     for ix, char in enumerate(word):
#         if char == BACKSPACE:
#             word.pop(ix)  # does not store anything
#             # worst case is if you remove the first element, pop(0) takes O(n) time
#             # pop(k) takes O(k) time <- removes the element at k and moves every element beyond k one position up
#             # pop(-1) takes O(1) time
#             # if using Queue structure, then use deque. It has constant time pop from both ends
#             how_many_to_delete += 1
#         else:
#             if how_many_to_delete > 0:
#                 word.pop(ix)
#                 how_many_to_delete -= 1

#     return word

# 20 ms -> beats 98.37%
class MySolution:
    def clean_word(self, word: str):
        # the strings in python are immutable
        lw, skip, new_word = len(word), 0, array("B")
        for i in range(lw - 1, -1, -1):
            ordinal = ord(word[i])
            if ordinal == BACKSPACE: skip += 1
            elif skip > 0:           skip -= 1
            else:                    new_word.append(ordinal)
        return new_word
    def main(self, S: str, T: str): return self.clean_word(S) == self.clean_word(T)

# 16 ms solution
# class Solution1:
#     def backspaceCompare(self, S: str, T: str) -> bool:
#         return self.editorProcessor(S) == self.editorProcessor(T)
#     def editorProcessor(self, string: str) -> str:
#         res, l = collections.deque(), 0
#         for i in string:
#             if i == "#":
#                 if  l > 0: 
#                     res.pop()
#                     l -= 1
#             else:
#                 res.append(i)
#                 l += 1
#         return ''.join(list(res))
# class MyAmendedSolution1:
#     # - above we are performing unnecessary O(n) operation: ''.join(list(res)). We can compare the strings in the list directly
#     # - when we compare the two strings, we can also terminate earlier if the length does not match
#     # to check length it takes O(1) || if any of the letters at the same indices mismatch
#     def backspaceCompare(self, S: str, T: str) -> bool: return self.process(S) == self.process(T)
#     def process(self, string: str) -> Iterable[str]:
#         res, l = [], 0
#         for s in string:
#             if s == "#":
#                 if l > 0:
#                     res.pop()
#                     l -= 1
#             else:
#                 res.append(s)
#                 l += 1
#         return res

# 12 ms solution
# class Solution:
#     def backspaceCompare(self, S: str, T: str) -> bool:
#         def finalStr(s: str):
#             stack = []
#             for char in s:
#                 if stack and char == '#':
#                     stack.pop()
#                 elif char != '#':
#                     stack.append(char)
#             return stack
#         return finalStr(S) == finalStr(T)

# However all of the above solutions take O(M + N) space

# Here is a two pointer approach for O(1) space


if __name__ == "__main__":
    test_cases = {
        ("##a", "a"):     True,
        ("##a#", ""):     True,
        ("a##b", "b"):    True,
        ("cd##", ""):     True,
        ("#######", ""):  True,
        ("cab##", "c"):   True,
        ("ab##c", "##c"): True,
    }

    for test_case, expected in test_cases.items():
        s = MySolution()
        actual = s.main(test_case[0], test_case[1])
        assert actual == expected, f"expected:{expected},actual:{actual}"
