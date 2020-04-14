#!/usr/bin/env python
from array import array
from typing import List, Optional


class Stack:
    def __init__(self):             self.stack = []
    def push(self, x: int) -> None: self.stack.append(x)
    def pop(self) -> Optional[int]:
        if not self.stack:          return None
        else:                       return self.stack.pop()
    def top(self) -> Optional[int]:
        if not self.stack:          return None
        else:                       return self.stack[-1]
    def __repr__(self): return f"Stack([{self.stack}])"


def main(n1: List[int], m: int, n2: List[int], n: int) -> List[int]:
    lix, rix = 0, 0
    stack = Stack()

    while lix < m and rix < n:
        print(f"n1:{n1},stack:{stack}")
        if stack.top() is not None:
            top = stack.pop()
            if top < n1[lix]:
                stack.push(n1[lix])
                n1[lix] = top
                lix += 1
                continue
            if top < n2[rix]:
                stack.push(n1[lix])
                n1[lix] = top
                lix += 1
            else:
                stack.push(n1[lix])
                n1[lix] = n2[rix]
                lix += 1
                rix += 1
    # stack top is None
        else:
            if n1[lix] <= n2[rix]: lix += 1
            # n2[rix] > n1[lix]
            else:
                stack.push(n1[lix])
                n1[lix] = n2[rix]
                lix += 1
                rix += 1

    while stack.top() and n2[rix:]:
        top = stack.pop()
        if top < n2[rix]:
            n1[lix] = top
            lix += 1
        else:
            n1[lix] = n2[rix]
            lix += 1
            rix += 1
    while n2[rix:]:
        n1[lix] = n2[rix]
        lix += 1
        rix += 1
    while stack.top():
        n1[lix] = stack.pop()
        lix += 1

    return n1


# def main(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
#     r = array('B')  # ? there are other typecodes, when would you want to have a higher minimum size in bytes?
#     lix, rix = 0, 0
#     while lix < m and rix < n:
#         if nums1[lix] < nums2[rix]: r.append(nums1[lix]); lix += 1
#         else:                       r.append(nums2[rix]); rix += 1
#     while lix < m: r.append(nums1[lix]); lix += 1
#     while rix < n: r.append(nums2[rix]); rix += 1
#     return r
# ! mistake 1: did not read the objective carefully enough
# ! it is asked to merge nums2 INTO nums1

# def main(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
#     lix, rix = 0, 0
#     stack = Stack()
#     # we compare nums1[lix] to nums2[rix]
#     # if we need to overwrite the value in nums1[lix], we could
#     # push all values down and make space for new value, this is expensive
#     # it is better to store a temporary buff for nums1 against
#     # which to check the values from nums2. Only the values that
#     # are overwritten go into that stack (this should be a stack)
#     while lix < m and rix < n:
#         # if there is something in the stack, then we have to check that first
#         if stack.top():
#             if stack.top() < nums2[rix]:
#                 temp = nums1[lix]
#                 nums1[lix] = stack.pop()
#                 if temp != 0: stack.push(temp)
#                 lix += 1
#             else:
#                 temp = nums1[lix + 1]
#                 nums1[lix + 1] = nums2[rix]
#                 if temp != 0: stack.push(temp)
#                 rix += 1
#                 lix += 1
#         else:
#             # this is ok, no need to push anything to stack
#             if nums1[lix] < nums2[rix]:
#                 lix += 1
#             # we are overwriting the value in nums1
#             else:
#                 if nums1[lix] != 0: stack.push(nums1[lix])
#                 nums1[lix] = nums2[rix]
#                 rix += 1
#                 lix += 1

#     # ! mistake 2: did not extend the other values here from stack
#     # ! mistake 3: did not increment lix in the while loop below
#     # ! mistake 4: while stack.top() returned False because top element was zero.. Check that it is not None!
#     # ! mistake 5: did not extend the values from nums2
#     # ! mistake 6: zeros are not considered part of nums1!! and I can move into them and then every number in nums2 would be larger than 0
#     # ! mistake 7: need to increment lix everywhere

#     if nums1[lix + 1] == 0:
#         # means we may have something in the stack that we can compare to nums2
#         if stack.top():
#             while stack.top() is not None:
#                 top = stack.pop()
#                 if rix < n:
#                     if top < nums2[rix]:
#                         nums1[lix + 1] = top
#                     else:
#                         nums1[lix + 1] = nums2[rix]
#                 else:
#                     nums1[lix + 1] = top
#                 lix += 1

#     if nums2[rix:]:
#         while rix < n:
#             nums1[lix] = nums2[rix]
#             lix += 1
#             rix += 1

#     return nums1


if __name__ == '__main__':
    nums1, nums2 = [1,2,3,0,0,0], [1,1,1]
    m, n = 3, 3
    r = main(nums1, m, nums2, n)
    print(r)
