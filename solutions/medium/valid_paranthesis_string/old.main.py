#!/usr/bin/env python
# from copy import deepcopy as dc
# from collections import deque
# from typing import Iterable, List
# import math

# from solutions.minions import verbose

# ! Attempt 2
# the subproblem is to generate +1 "(", -1 ")" and 0 "" (when removing *) combinations
# that will keep the parantheses balanced. If no such combinations exist, return False
# for the combinations that exist, perform a vanilla parantheses checks on all
# if any is True, return True
# @verbose
# def bracket_selection_generator(
#     s: Iterable[str],
#     balance: int,
#     star_indices: Iterable[int],
#     stars: int,
# ) -> List[str]:
#     if s[-1] == '(' or s[0] == ')': return
#     if stars == 0 and "*" in s:
#         print(f"s:{s},balance:{balance},star_indices:{star_indices},stars:{stars}")
#         raise Exception
#     if stars   == 0:
#         yield s
#         return
#     if balance == 0:
#         s = "".join(s)
#         s = s.replace(" ", "").replace("*", "")
#         yield deque(s)
#         return

#     while len(star_indices) > 0:  # 💡 if what remains after application of delta is fixable by remaining stars
#         curr_num_of_stars = len(star_indices)
#         if math.fabs(balance + 1) <= curr_num_of_stars - 1:
#             s_ = dc(s)
#             si = dc(star_indices)
#             star_index = si.popleft()
#             s_[star_index] = "("
#             yield from bracket_selection_generator(s_, balance + 1, si, curr_num_of_stars - 1)
#         if math.fabs(balance - 1) <= curr_num_of_stars - 1:
#             s_ = dc(s)
#             si = dc(star_indices)
#             star_index = si.popleft()
#             s_[star_index] = ")"
#             yield from bracket_selection_generator(s_, balance - 1, si, curr_num_of_stars - 1)
#         leftest_star_index = star_indices.popleft()
#         if s[leftest_star_index] == "*":
#             del s[leftest_star_index]
#             star_indices = deque([x - 1 for x in star_indices])

# def standard_parantheses_checker(s: str) -> bool:
#     stack = []
#     for c in s:
#         if c == "(":             stack.append(c)
#         elif stack and c == ")": stack.pop()
#         else:                    return False
#     return stack == []


# @verbose
# def is_valid(s: str) -> bool:
#     if s and s[-1] == '(' or (s and s[0] == ")"): return False
#     star_indices, d = deque(), deque()
#     possibilities = []
#     balance, stars = 0, 0
#     for ix, char in enumerate(s):
#         if d and d[-1]  == "("  and char == ")": balance -= 1; d.pop(); continue
#         elif char == " ": continue
#         elif char == "*": stars += 1; star_indices.append(len(d))
#         elif char == ")": balance -= 2
#         balance += 1
#         d.append(char)
#     balance -= stars
#     if balance == 0:
#         cond = standard_parantheses_checker(s)
#         if cond: return True
#     possibilities = bracket_selection_generator(d, balance, star_indices, stars)
#     for p in possibilities:
#         print(p)
#         if standard_parantheses_checker(p): return True
#     return False


# class StackWithStars(Stack):
#     def __init__(self):
#         super().__init__()
#         self.stars = []

#     def push(self, x):
#         if x == "*":
#             self.stars.append(len(self.stack))
#         super().push(x)


# def possible_stacks(stack: StackWithStars, all_stacks: List[StackWithStars] = None):
#     if all_stacks is None: all_stacks = []
#     if not stack.stars:    all_stacks.append(stack); return
#     one_star = stack.stars.pop()

#     no_star_stack   = dc(stack)
#     new_left_stack  = dc(stack)
#     new_right_stack = dc(stack)

#     new_left_stack.stack[one_star]  = "("
#     new_right_stack.stack[one_star] = ")"
#     del no_star_stack.stack[one_star]

#     possible_stacks(new_left_stack, all_stacks)
#     possible_stacks(new_right_stack, all_stacks)
#     possible_stacks(no_star_stack, all_stacks)

#     return all_stacks


# def is_valid_stack(stack: StackWithStars):
#     all_stacks = possible_stacks(stack)
#     for stack in all_stacks:
#         top_values = deque()
#         # stack is (()). what happens?
#         while len(stack) > 0:
#             top = stack.pop()
#             if top_values:
#                 if top == "(" and top_values[0] == ")":
#                     top_values.popleft()
#                     continue
#             top_values.append(top)
#         if len(top_values) == 0 and len(stack) == 0: return True
#     return False


# ! Attempt 1
# def is_valid(s: str):
#     if s[0] == ")": return False
#     stack = StackWithStars()
#     for char in s:
#         if char == ")" and stack.top() == "(": stack.pop(); continue
#         elif char == " ": continue
#         stack.push(char)
#     return len(stack) == 0 or is_valid_stack(stack)

# -------
# def is_valid(s: str, stack: Optional[Stack] = Stack(), loop_from_ix: int = 0) -> bool:
#     while loop_from_ix < len(s):
#         char = s.popleft()
#         if char == '*':
#             return any(
#                 (
#                     is_valid(s, dc(stack)),
#                     is_valid(s, stack),
#                 )
#             )
#         if stack.top() == "(" and char == ")": stack.pop()
#         elif char == " ": continue
#         else:                                stack.push(char)
#         loop_from_ix += 1
#     return len(stack) == 0


# if __name__ == '__main__':
    # is_valid("(*()")
    # is_valid("(*))")
    # is_valid("()")
    # is_valid("((*)")
    # is_valid("(*)")
    # is_valid("(((******))")
    # is_valid("*()**(")
    # is_valid("(())()())(*))(((((())()*))**))**()(*(()()*)(**(())()**)((**(()(((()()**)())*(*))(())()()*")
    # is_valid("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()")
