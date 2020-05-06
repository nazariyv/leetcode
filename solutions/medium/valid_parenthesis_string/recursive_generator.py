#!/usr/bin/env python
from typing import Generator


def yield_nums(s: str = "", stars: int = 3) -> Generator[str, None, None]:
    if stars == 0: yield s; return

    while stars > 0:
        yield from yield_nums(")" + s, stars - 1)
        yield from yield_nums("(" + s, stars - 1)
        stars -= 1


if __name__ == '__main__':
    for num in yield_nums(): print(num)
