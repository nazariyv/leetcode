#!/usr/bin/env python
import logging
from solutions.minions import Style

log = logging.getLogger("valid_parenthesis")

# "(": [1], "(*": [0, 1, 2], "(**": [0, 1, 2, 3], "(**)": [0, 1, 2]
# ")": [-1] imbalanced, "())": [-1] imbalanced
def is_valid(s: str) -> bool:
    lo, hi = 0, 0
    for c in s:
        if   c == "(": lo += 1; hi += 1
        elif c == ")": lo -= 1; hi -= 1
        elif c == "*": lo -= 1; hi += 1
        elif c == " ": continue
        else: raise Exception("never")
        if hi < 0: return False
        lo = max(lo, 0)
    return lo == 0


if __name__ == '__main__':
    test_cases = {
        "()": True,
        "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()": True,
        "(*)": True,
        "": True,
        " ": True,
        "(": False,
        ")": False,
        "((": False,
        "))": False,
        "))(": False,
        "*": True,
        ")*(": False,
        ")**(": False,
        "(*))": True,
        "((*)": True,
        "*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)": False,
        "(*()()())(((*(()((((()())()()*()(())))))(((*(()*)())((())))(((()))))*)))((()())(*())**((())))(*)": True, # ! mistake 3
        "(())((())()()(*)(*()(())())())()()((()())((()))(*": False,
        "(()*)(()((())()))(*)((((())*())))()(((()((()(*()))": False,
        "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())": False,
        "((((((((((((((())(((((()))()))))))))(((((((()(((*)": False,
    }

    for test, expected in test_cases.items():
        actual = is_valid(test)
        styler = Style.GREEN if actual == expected else Style.RED
        log.info(styler(f"actual:{actual},expected:{expected},test:{test}"))
