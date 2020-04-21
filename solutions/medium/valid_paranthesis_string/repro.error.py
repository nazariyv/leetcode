#!/usr/bin/env python
from typing import Generator


def combo_generator(s: str, stars: int) -> Generator[str, None, None]:
    if stars == 0:
        print(s)
        yield s
        return
    else:
        star_ix       = s.find("*")
        left_part     = s[:star_ix]
        right_part    = s[star_ix + 1:]
        open_bracket  = left_part + "(" + right_part
        close_bracket = left_part + ")" + right_part
        no_bracket    = left_part + right_part
        yield from combo_generator(no_bracket,    stars - 1)
        yield from combo_generator(open_bracket,  stars - 1)
        yield from combo_generator(close_bracket, stars - 1)
        return


if __name__ == '__main__':
    test = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())"
    stars = 0
    for char in test:
        if char == "*": stars += 1
    print(stars)
    print(list(combo_generator(test, stars)))
