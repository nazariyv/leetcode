#!/usr/bin/env python
from typing import List, Tuple

Shift = Tuple[int, int]


# succinter
# class Solution:
#     def stringRotation(self, s: str, rotation: List[List[int]]) -> str:
#         chars = collections.deque(s)
#         for d, amount in rotation:
#             if d == 0:
#                 for _ in range(amount):
#                     num = chars.popleft()
#                     chars.append(num)
#             else:
#                 for _ in range(amount):
#                     num = chars.pop()
#                     chars.appendleft(num)
#         return ''.join(chars)

def net_effect(l: List[Shift]) -> int:
    net_shift = 0
    for op in l:
        if op[0] == 0: net_shift -= op[1]
        else:          net_shift += op[1]
    return net_shift


# net_shift = 3, but length 2, then net shift is in fact 1: 3 % 2
# net_shift = 4, but length 2, then net shift is zero
# what if net_shift is < 0
def shift_string(to_shift: str, shift: List[Shift]) -> str:
    to_shift_len = len(to_shift)
    net_shift    = net_effect(shift)
    net_shift    = net_shift % to_shift_len if net_shift > 0 else -(-net_shift % to_shift_len)
    # O(n)
    if net_shift > 0: return "".join(
        (
            to_shift[to_shift_len - net_shift:],
            to_shift[:to_shift_len - net_shift],
        )
    )
    if net_shift < 0: return "".join(
        (
            to_shift[-net_shift:],
            to_shift[:-net_shift],
        )
    )
    # O(1)
    return to_shift


if __name__ == '__main__':
    l = [(1,1), (1,1), (0,2), (1,5)]
    r = shift_string("dog", l)
    print(r)
