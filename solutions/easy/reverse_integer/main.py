#!/usr/bin/env python
from solutions.minions import Style, verbose
import logging

log = logging.getLogger("reverse_integer")

C = 2 ** 31
LL, UL = -C, C - 1


# O(log_10(x))
@verbose
def main(x: int) -> int:
    s = str(abs(x))
    a = int(s[::-1])
    a = -a if x < 0 else a
    if a < LL or a > UL: return 0
    return a


if __name__ == '__main__':
    test_cases = {
        123: 321,
        -123: -321,
        120: 21,
        LL: 0,
        UL: 0,
    }

    for test, expected in test_cases.items():
        actual = main(test)
        styler = Style.GREEN if actual == expected else Style.RED
        log.info(styler(f"actual:{actual},expected:{expected},test:{test}"))
