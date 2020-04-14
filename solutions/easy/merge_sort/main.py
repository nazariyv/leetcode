#!/usr/bin/env python
from typing import List

def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    lix,rix, ll, lr = 0,0, len(left),len(right)
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

if __name__ == '__main__':
    print(merge_sort([-1,2,10,222,-2,3,20]))