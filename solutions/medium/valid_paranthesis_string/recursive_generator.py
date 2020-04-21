#!/usr/bin/env python
from solutions.minions import verbose

def yield_nums(s: str = "", stars = 3):
    if stars == 0: yield s; return

    while stars > 0:
        yield from yield_nums(")" + s, stars - 1)
        yield from yield_nums("(" + s, stars - 1)
        stars -= 1


if __name__ == '__main__':
    for num in yield_nums(): print(num)
