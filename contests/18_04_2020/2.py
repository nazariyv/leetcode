#!/usr/bin/env python
from solutions.minions import Style
from typing import Generator
import logging

log = logging.getLogger("sss")


# 1 <= n <= 10
# 1 <= k <= 100
def lexi_happy_gen(n: int, s: str = "") -> Generator[str, None, None]:
    if n == 0: yield s; return
    prev_letter = ""
    if s: prev_letter = s[-1]
    if prev_letter != "a": yield from lexi_happy_gen(n - 1, s + "a")
    if prev_letter != "b": yield from lexi_happy_gen(n - 1, s + "b")
    if prev_letter != "c": yield from lexi_happy_gen(n - 1, s + "c")

def getHappyString(n: int, k: int) -> str:
    curr_k = 0
    result = ""
    gen = lexi_happy_gen(n)
    while curr_k != k:
        try:              result = next(gen)
        except Exception: return ""
        curr_k += 1
    return result

if __name__ == '__main__':
    test_cases = {
        (1, 1): "a",
        (1, 2): "b",
        (1, 3): "c",
        (1, 4): "",
        (3, 9): "cab",
        (2, 7): "",
        (10, 100): "abacbabacb",
    }

    for test, expected in test_cases.items():
        actual = getHappyString(test[0], test[1])
        styler = Style.GREEN if actual == expected else Style.RED
        log.info(styler(f"actual:{actual},expected:{expected},test:{test}"))
