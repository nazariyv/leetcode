#!/usr/bin/env python
from typing import List, Tuple


class StockSpanner(object):
    def __init__(self) -> None:
        self.stack: List[Tuple[int, int]] = []

    def next(self, price: int) -> int:
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight


if __name__ == '__main__':
    ...
