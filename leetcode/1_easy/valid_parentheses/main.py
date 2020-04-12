#!/usr/bin/env python
from collections import defaultdict
from leetcode.minions import Stack

left_right = {
    '(': ')',
    '{': '}',
    '[': ']',
}

right_left = {
    ')': '(',
    '}': '{',
    ']': '[',
}

left  = {'(', '{', '['}
right = {')', '}', ']'}


class FunAndSlowSolution:
    def isValid(self, s):
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        return s == ''


# BEST
class Solution:
    def isValid(self, s: str) -> bool:
        my_map, stack = {"(": ")", "[": "]", "{": "}"}, []
        for c in s:
            if c in my_map:                        stack.append(c)
            elif stack and c == my_map[stack[-1]]: stack.pop()
            else:                                  return False
        return stack == []


def is_valid(s: str) -> bool:
    stack = Stack()
    for c in s:
        if c in left:
            top = stack.top()
            if top is None: stack.push(c)
            else:
                if c not in left: return False
                stack.push(c)
        elif c in right:
            top = stack.pop()
            if right_left[c] != top: return False
        else:
            if c != ' ': raise Exception('never') 
    return len(stack) == 0

# def is_valid(s: str) -> bool:
#     # '(()())'
#     # ')()('  # look for symmetry and ensure that they balance. i.e. cannot sum with the first negative number like -11
#     # ''
#     n = len(s)              #   [],(),{},[[,((,
#                             #   )), ]]
#     if n == 2:
#         return  any(left_right[s[0]] == s[1], s[0] == s[1])
#     return is_valid()




# (()) # the first closing bracket should match the prev
# )    # if starts with ),},] is not valid
# ()() # the one after the first closing does not have to be closing
# 

# * TIP: Look for symmetry & invariants. For example, in this problem, it was important to notice the
# * symmetry around the mid point. That is the solution
# ! mistake 1: understand the conditions correctly. I misunderstood the condition about the order
# ! mistake 2: patching up bugs and running main instead of carefully thinking about the consequences of the patch
# ! for example, I thought that if the current bracket is one of ), }, ] and the previous is on the elft
# ! then the left one must be the corresponding one, which is correct, but which does not cover a case like the
# ! like the following: "[([{]])". And so I have to work around the symmetry axis!
# ! find a mid point and ensure that the brackets reflect correctly.
# def is_valid(s: str) -> bool:
#     if s == "": return True
#     balance, left, key = defaultdict(int), {'(', '{', '['}, None
#     for ix, c in enumerate(s):
#         if c in left:
#             balance[c] += 1
#         elif c == ' ': continue
#         else:
#             if ix - 1 >= 0:
#                 prev = s[ix - 1]
#                 if (prev in left) and (left_right[prev] != c):
#                     return False
#             key = right_left[c]
#             balance_score = balance[key] - 1
#             if balance_score < 0: return False
#             else:                 balance[key] = balance_score
#     return all(0 == x for x in list(balance.values()))


if __name__ == '__main__':
    test_cases = {
        "(( ))": True,
        "({[]})": True,
        "(({[]}))": True,
        "()()": True,
        "(()(){)": False,
        "([][])": True,
        "{([]())}": True,
        "{]}": False, 
        "}": False,
        "{": False,
        "([)]": False,
        "[([]])": False, # [)
    }

    for case, expected in test_cases.items():
        actual = is_valid(case)
        print(case)
        assert actual == expected, f"actual:{actual}, expected:{expected}"
