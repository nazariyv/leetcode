#!/usr/bin/env python
from typing import List


# this operation is
# time:  O(n)
# space: O(1)
def top_2_max(l: List[int]):
    maxest,next_max = [0, 0,], [0, 0,]
    for i in range(0, len(l)):
        if l[i]   > maxest[0]:   next_max = maxest; maxest = [l[i], i]
        elif l[i] > next_max[0]: next_max = [l[i], i]
    if maxest[1]  < next_max[1]: next_max[1] -= 1
    return maxest, next_max


# t:O(n+2k),s:O(1)
def smash_two_stones(stones: List[int]) -> int:
    maxest, next_max = top_2_max(stones) # t:O(n),s:O(1)
    smash = maxest[0] - next_max[0]
    # pops are O(k) each
    stones.pop(maxest[1])   # after I pop one, the index of the other may change
    stones.pop(next_max[1])
    # O(1)
    if smash > 0: stones.append(smash)
    return stones

# O(n - 1 * (n + 2 * max({k_i forall i in I})))
# denote max({k_i forall i in I}) as K, then
# O((n - 1) * (n + 2K))
# O(n ** 2 + 2nK - n - 2K)
# O(n ** 2) in time and O(1) in space
# t=O(n ** 2)
# s=O(1)
def main(stones: List[int]) -> int:
    n = len(stones)
    if   n < 1: return 0
    elif n < 2: return stones[0]
    # O(n - 1)
    while n > 1:
        # O(n + 2k)
        stones = smash_two_stones(stones)
        n = len(stones)
    return 0 if n == 0 else stones[0]

# O(n) time
# O(1) space
# ! mistake 1: do not mutate list as you loop through it
# def main(stones: List[int]) -> int:
#     while len(stones) > 1:
#         maxest, next_max = top_2_max(stones)
#         smash = maxest[0] - next_max[0]
#         stones.pop(maxest[1])
#         stones.pop(next_max[1])
#         if smash != 0: stones.append(smash)
#         else:          continue
#     return 0 if len(stones) == 0 else stones[0]


if __name__ == '__main__':
    test_cases = [
        ([5,5], 0),
        ([5,4], 1),
        ([3], 3),
        ([], 0),
        ([10,8,2,1], 1),
    ]

    for case, expected in test_cases:
        actual = main(case)
        print(f"case:{case},expected:{expected},actual:{actual}")
        assert actual == expected, f"actual:{actual},expected:{expected}"
