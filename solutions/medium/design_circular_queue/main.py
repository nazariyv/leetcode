#!/usr/bin/env python
from typing import List

SMOL = -2 ** 31

class MyCircularQueue:

    __slots__ = ('_q', '_head', '_head', '_tail', '_k', '_q_len')

    def __init__(self, k: int) -> None:
        self._q: List[int] = [SMOL] * k
        self._head = [SMOL, SMOL]  # value and idx
        self._tail = [SMOL, SMOL]  # value and idx
        self._k = k
        self._q_len = 0

    def __repr__(self) -> str:
        return "|".join([str(x) for x in self._q])

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        appended_at_idx = (self._tail[1] + 1) % self._k
        self._q[appended_at_idx] = value
        self._tail = [self._q[appended_at_idx], appended_at_idx]
        if self._q_len == 0: self._head = self._tail
        self._q_len += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self._q[self._head[1]] = SMOL
        self._head[1] = (self._head[1] + 1) % self._k
        self._head[0] = self._q[self._head[1]]
        if self._q_len == 1: self._tail = [SMOL, SMOL]
        self._q_len -= 1
        return True

    def Front(self) -> int: return self._head[0]
    def Rear(self) -> int: return self._tail[0]
    def isEmpty(self) -> bool: return self._q_len == 0
    def isFull(self) -> bool: return self._q_len == self._k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


if __name__ == '__main__':
    mcq = MyCircularQueue(3)
    mcq.Front()
    mcq.Rear()
    mcq.deQueue()
    mcq.enQueue(1)
    mcq.enQueue(2)
    mcq.deQueue()
    mcq.Front()
    mcq.Rear()
    mcq.enQueue(3)
    mcq.enQueue(4)
    mcq.enQueue(5)
    mcq.Front()
    mcq.Rear()
    ...