#!/usr/bin/env python
from solutions.minions import verbose, Style
import logging

log = logging.getLogger("roman_to_integer")

roman_to_integer = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

combos = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}


@verbose
def main(s: str) -> int:
    if len(s) == 0: return 0
    if len(s) == 1: return roman_to_integer[s[0]]
    run_sum = 0
    skip = False
    for i in range(1, len(s)):
        if skip: skip = False; continue
        two_letters = s[i-1] + s[i]
        if two_letters in combos:
            run_sum += combos[two_letters]
            skip = True
        else:
            run_sum += roman_to_integer[s[i-1]]
    # ! mistake 1. did not count the last elem
    if not skip: run_sum += roman_to_integer[s[-1]]
    return run_sum


if __name__ == '__main__':
    test_cases = {
        "III": 3,
        "IV": 4,
        "IX": 9,
        "X": 10,
        "MIX": 1009,
        "MCMXCII": 1992,
        "MCMXCVII": 1997,
    }
    for test, expected in test_cases.items():
        actual = main(test)
        styler = Style.GREEN if actual == expected else Style.RED
        log.info(styler(f"actual:{actual},exptected:{expected},test:{test}"))
