#!/usr/bin/env python
from solutions.minions import TestCase as T, TestRunner as TR
import logging

log = logging.getLogger("valid_parenthesis_star")

mapper = {
    "(": 1,
    ")": -1,
    " ": 0,
    "*": 0,
}

def local_problems(s: str) -> Generator[str, None, None]:
    ...

def valid_parenthesis(s: str) -> bool:
    if not s: return True
    if s[0] == ")" or s[-1] == "(": return False
    balance = 0
    num_stars = 0
    for char in s: balance += mapper[char]
    log.debug(f"the balance value is: {balance}")
    if balance == 0: return True
    elif num_stars >= abs(balance): return True
    return False


if __name__ == '__main__':
    TR(
        (
            T("()", True),
            T("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()", True),
            T("(*)", True),
            T("", True),
            T(" ", True),
            T("((", False),
            T(")", False),
            T("*", True),
            T(")*(", False),
            T("))**((", False),
            T("(*))", True),
            T("((*)", True),
            T("*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)", False),
            T("(*()()())(((*(()((((()())()()*()(())))))(((*(()*)())((())))(((()))))*)))((()())(*())**((())))(*)", True),
            T("(())((())()()(*)(*()(())())())()()((()())((()))(*", False),
            T("(()*)(()((())()))(*)((((())*())))()(((()((()(*()))", False),
            T("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())", False),
            T("((((((((((((((())(((((()))()))))))))(((((((()(((*)", False),
        ),
        valid_parenthesis
    )()
