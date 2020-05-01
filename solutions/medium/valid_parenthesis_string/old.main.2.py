#!/usr/bin/env python
from solutions.minions import verbose, Style
from typing import List, Optional, Generator, Tuple
from collections import deque
import logging

log = logging.getLogger("valid_parenthesis")

# O(n) space and O(n) time
@verbose
def reduce(s: str) -> Tuple[str, int]:
    """reduces the problem. for example "((()*))" -> "((*))"
    """
    if len(s) < 2: return s, 0
    stack: List[str] = []
    num_of_stars_in_reduced = 0
    for char in s:
        if stack and stack[-1] == "(" and char == ")": stack.pop(); continue
        if char == "*": num_of_stars_in_reduced += 1
        stack.append(char)
    if stack and stack[0]  == "*":
        stack[0]  = "("
        num_of_stars_in_reduced -= 1
    if stack and stack[-1] == "*":
        stack[-1] = ")"
        num_of_stars_in_reduced -= 1
    return "".join(stack), num_of_stars_in_reduced

# O(n) space and O(n) time
@verbose
def divide(s: str) -> List[List[str]]:
    """divides the problem into subproblems. "(())()(())" -> ["(())", "()", "(())"]
    """
    if len(s) < 2: return [s]
    curr, subproblems = deque(s[0]), []  # ! mistake 1: did not include the first element in the deque
    for i in range(1, len(s)):
        si = s[i]
        if s[i-1] == ")" and si == "(":
            subproblems.append("".join(curr))
            curr = deque(["("])
        elif si == " ": continue
        else:           curr.append(si)
    subproblems.append("".join(curr))
    return subproblems

@verbose
def primtive_cheks(s: str) -> Optional[bool]:
    if s == "" or s == " ":         return True
    if len(s) == 1 and s[0] != "*": return False
    if s[0] == ")" or s[-1] == '(': return False
    return None

@verbose
def combo_generator(s: str, stars: int) -> Generator[str, None, None]:
    if stars == 0:
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

@verbose
def slow_is_valid(s: str) -> bool:
    if len(s) == 0: return True
    stack = []
    for char in s:
        if char == " ": continue
        elif stack and char == ")" and stack[-1] == "(": stack.pop(); continue
        stack.append(char)
    return len(stack) == 0

# O(k) space and O(k) time where k is the subproblem size
@verbose
def fast_is_not_valid(s: str) -> bool:
    primtive = primtive_cheks(s)
    if primtive is not None: return primtive
    balance, num_of_stars = 0, 0
    for char in s:
        if char == "*":   num_of_stars += 1
        elif char == "(": balance += 1
        elif char == ")": balance -= 1
        else:             raise Exception("unknown character")
    if num_of_stars < abs(balance):
        return False
    return True

@verbose
def main(s: str) -> bool:
    reduced, num_of_stars = reduce(s)
    subproblems = divide(reduced)
    fast = all(fast_is_not_valid(subprob) for subprob in subproblems)  # ! mistake 2: should be all. was any
    if not fast:
        combos = combo_generator(reduced, num_of_stars)
        print(list(combos))
        # return any(slow_is_valid(combo) for combo in combos)
    return True


if __name__ == '__main__':
    test_cases = {
        # "()": True,
        # "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()": True,
        # "(*)": True,
        # "": True,
        # " ": True,
        # "(": False,
        # ")": False,
        # "((": False,
        # "))": False,
        # "))(": False,
        # "*": True,
        # ")*(": False,
        # ")**(": False,
        # "(*))": True,  # ! mistake 1,
        # "((*)": True,
        # "*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)": False, # ! mistake 2
        # "(*()()())(((*(()((((()())()()*()(())))))(((*(()*)())((())))(((()))))*)))((()())(*())**((())))(*)": True, # ! mistake 3
        # "(())((())()()(*)(*()(())())())()()((()())((()))(*": False,
        # "(()*)(()((())()))(*)((((())*())))()(((()((()(*()))": False,
        "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())": False,
        # "((((((((((((((())(((((()))()))))))))(((((((()(((*)": False,
    }

    for test, expected in test_cases.items():
        actual = main(test)
        styler = Style.GREEN if actual == expected else Style.RED
        log.info(styler(f"actual:{actual},expected:{expected},test:{test}"))

# ! time limit exceeded when looping through the longer ones