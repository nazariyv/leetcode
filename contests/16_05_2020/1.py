#!/usr/bin/env python
from solutions.minions import TestRunner as TR, TestCase as T


def maxPower(s: str) -> int:
    # ""
    # "abcd"
    # "aabaaa"
    
    longest_sub_len = 1
    longest_char = ""
    
    curr_sub_len = 1
    curr_char = s[0]
    
    stck = [curr_char]
    
    for char in s[1:]:
        if char == stck[-1]:
            curr_sub_len += 1

            if curr_sub_len > longest_sub_len:
                longest_sub_len = curr_sub_len
                longest_char = char
        
        else:
            _ = stck.pop()
            stck.append(char)
            curr_char = char
            curr_sub_len = 1

    return longest_sub_len


if __name__ == '__main__':
    TR(
        (
            T("aabaa", 2),
            T("tourist", 1),
            T("abc", 1),
            T("leetcode", 2),
            T("hooraaaaaaaaaaay", 11),
        ),
        maxPower
    )()
    ...