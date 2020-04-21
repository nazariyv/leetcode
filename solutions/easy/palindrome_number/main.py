#!/usr/bin/env python
from solutions.minions import Style, verbose
import logging

log = logging.getLogger("palindrom_number")


# to solve without converting to a stirng check if the reverted second half matches the first half
# starts from outwards and goes inwards
@verbose
def main(x: int) -> bool:
    x = str(x)
    n, ix = len(x), 0
    if n < 2: return True
    if n == 2: return x[0] == x[-1]
    while ix < n // 2:
        if x[ix] != x[n - 1 - ix]: return False
        ix += 1
    return True


if __name__ == '__main__':
    test_cases = {
        1: True,
        22: True,
        1221: True,
        121: True,
        123: False,
        12344321: True,
        0: True,
        23123123123: False,
    }

    for test, expected in test_cases.items():
        actual = main(test)
        styler = Style.GREEN if actual == expected else Style.RED
        log.info(styler(f"actual:{actual},expected:{expected},test:{test}"))
