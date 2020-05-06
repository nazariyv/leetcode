#!/usr/bin/env python


# def checkIfCanBreak(s1: str, s2: str) -> bool:
#     sorted1 = sorted(s1)
#     sorted2 = sorted(s2)
#     result = 0
#     for idx in range(len(s1)):
#         if sorted1[idx] < sorted2[idx]:
#             if result not in (0, 1):
#                 return False
#             result = 1
#         elif sorted1[idx] > sorted2[idx]:
#             if result not in (0, -1):
#                 return False
#             result = -1
#     return True


def checkIfCanBreak(s1: str, s2: str) -> bool:
    s1s = sorted(s1)
    s2s = sorted(s2)
    return all(c1 >= c2 for c1, c2 in zip(s1s, s2s)) \
        or all(c2 >= c1 for c2, c1 in zip(s2s, s1s)) \


if __name__ == '__main__':
    print(checkIfCanBreak("abc", "xya"))
    print(checkIfCanBreak("abe", "acd"))
    print(checkIfCanBreak("leetcode", "interview"))
    print(checkIfCanBreak("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqpomnlkjihgfedcba"))
