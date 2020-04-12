#!/usr/bin/env python
from typing import List

class Number:
    def __init__(self, value, streak):
        self.value = value
        self.streak = streak
    def __str__(self):
        return f"{self.value}|{self.streak}"

# Given an integer array arr, count element x such that x + 1 is also in arr.
# If there are duplicates in arr, count them seperately.
# 1 <= arr.length <= 1000
# 0 <= arr[i] <= 1000
# [0,0,1,1,2,3]
# [1,1,2,3] # 2 so far, because 0 -> 1 and 0-> 1
# [1,2,3] . # 3 so far, because 1 -> 2, but can't pair the 1 with 2, because 2 was already paired with
# [1, 3] # answer is 4
def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    lix,rix, ll, lr = 0,0, len(left), len(right)
    while lix < ll and rix < lr:
        if left[lix] < right[rix]: result.append(left[lix]);  lix += 1
        else:                      result.append(right[rix]); rix += 1
    if left[lix:]:                 result.extend(left[lix:])
    if right[rix:]:                result.extend(right[rix:])
    return result
def merge_sort(l: List[int]) -> List[int]:
    n = len(l)
    if n < 2: return l
    mid = n // 2
    left, right = merge_sort(l[:mid]), merge_sort(l[mid:])
    return merge(left, right)

# [0,0,1,2,2,3,3,3] -> o: 0-1, 1-2, 2-3, 2-3 = 4
# [0,0,1,3,4,4,5]
# O(n * logn) time 
# O(n)        space
def main(arr: List[int]) -> int:
    n = len(arr)
    if n < 2: return 0
    arr = merge_sort(arr)  # O(n * logn). best, worst and average case. quicksort in practice is faster
    print(arr)
    num_consec_elems = 0
    prev = Number(value=arr[0], streak=1)
    first_seen_at = {}

    for i in range(1, n):
        if arr[i] not in first_seen_at: first_seen_at[arr[i]] = i - 1

        if arr[i] == prev.value:
            prev.streak += 1
        elif arr[i] == prev.value + 1:
            num_consec_elems += 1
            prev.streak -= 1
            if prev.streak == 0:
                prev.value  = arr[i]
                prev.streak = i - first_seen_at[arr[i]]
        else:
            if arr[i - 1] + 1 == arr[i]: num_consec_elems += 1
            prev.value  = arr[i]
            prev.streak = 1

        # print(f"prev={prev},curr={arr[i]},n={num_consec_elems},arr[i:]:{arr[i:]}")

    return num_consec_elems


if __name__ == "__main__":
    lst = {
        (0,1,2): 2,
        (1,1,2,2): 2,
        (0,0,1,2,2,3,3,3): 4,
        (0,1,4,4,5,5): 3,
        (): 0,
        (0,2,2,3,3,3,4,4,4,4): 5,
        (1,2,2,2,3,4,4,4,5,5,5,5,6,7): 8,
    }
    for l, expected in lst.items():
        actual = main(l)
        print(actual)
        assert actual == expected, f"actual:{actual},expected:{expected}"
