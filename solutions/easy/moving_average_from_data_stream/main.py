#!/usr/bin/env python
from __future__ import division
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self._d: deque = deque(maxlen=size)

    def next(self, val: int) -> float:
        self._d.append(val)
        return sum(self._d) / len(self._d)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


if __name__ == '__main__':
    m = MovingAverage(3)
    m.next(3)
    m.next(4)
    m.next(5)
    ...