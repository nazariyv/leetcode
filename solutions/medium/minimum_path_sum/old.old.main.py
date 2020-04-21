# #!/usr/bin/env python
# from solutions.minions import Style, verbose, TestRunner as TR, TestCase as T, bisect_left
# from collections import deque
# from sortedcontainers import SortedList
# from typing import List, Iterable
# from copy import deepcopy as dc
# import logging

# LARGE = 2 ** 32 - 1
# class Runner:
#     def __init__(self, pos: List[int], cumcost: int, traverse_path = None):
#         self.pos = pos
#         self.cumcost = cumcost
#         if traverse_path is None:
#             self.traverse_path = dc([self.pos])
#         else:
#             self.traverse_path = dc(traverse_path)
#     def go_down(self, delta_cost: int):
#         self.pos[0] = self.pos[0] + 1
#         self.cumcost += delta_cost
#         self.traverse_path = dc(self.traverse_path) + dc([self.pos])
#     def go_right(self, delta_cost: int):
#         self.pos[1] = self.pos[1] + 1
#         self.cumcost += delta_cost
#         self.traverse_path = dc(self.traverse_path) + dc([self.pos])
#     def __repr__(self):
#         return f"Runner(pos={self.pos},cumcost={self.cumcost},traverse_path={self.traverse_path})"
#     def __copy__(self):
#         return type(self)(self.pos, self.cumcost)
#     def __deepcopy__(self):
#         return type(self)(list(self.pos), self.cumcost, list(self.traverse_path))
# def cumcost_down(run: Runner, grid: List[List[int]]) ->  int:
#     try:
#         return run.cumcost + grid[run.pos[0] + 1][run.pos[1]]
#     except IndexError:
#         return LARGE
# def cumcost_right(run: Runner, grid: List[List[int]]) -> int:
#     try:
#         return run.cumcost + grid[run.pos[0]][run.pos[1] + 1]
#     except IndexError:
#         return LARGE
# def delta_down(run: Runner, grid: List[List[int]]) -> int:
#     try:
#         return grid[run.pos[0] + 1][run.pos[1]]
#     except IndexError:
#         return LARGE
# def delta_right(run: Runner, grid: List[List[int]]) -> int:
#     try:
#         return grid[run.pos[0]][run.pos[1] + 1]
#     except IndexError:
#         return LARGE
# def update_all_runners(run: Runner, all_runners: Iterable[Runner]) -> None:
#     # ! mistake 3: consider a scenario where you first insert 10 and then 20. The next elem is 15, you will insert it after 20
#     # ! need a proper algo for insertion O(log n) time
#     all_runners_cost = [runner.cumcost for runner in all_runners]
#     ix = bisect_left(all_runners_cost, run.cumcost)
#     all_runners.insert(ix, run)
# # ! mistake 1: noone said that there will be an order imposed on deque. You need to "order" it yourself!
# # ! mistake 2: indexing issues as writte in the TODO. Some clone runners cannot go to the right or down, in this case don't go anywhere!
# def min_path_sum(grid: List[List[int]]) -> int:
#     m, n = len(grid), len(grid[0])
#     curr_runner = Runner(pos=[0, 0], cumcost=grid[0][0])
#     all_runners = deque()
#     while curr_runner.pos[0] != m - 1 or curr_runner.pos[1] != n - 1:
#         down_cost    = cumcost_down(curr_runner, grid)
#         right_cost   = cumcost_right(curr_runner, grid)
#         optimal_cost = min(down_cost, right_cost)
#         if len(all_runners) > 0:
#             next_runner = all_runners[-1]
#             down_cost_next_runner = cumcost_down(next_runner, grid)
#             right_cost_next_runner = cumcost_right(next_runner, grid)
#             if any(cost < optimal_cost for cost in [down_cost_next_runner, right_cost_next_runner]):
#                 new_runner = all_runners.pop()
#                 update_all_runners(curr_runner, all_runners)
#                 curr_runner = new_runner
#         down_delta  = delta_down(curr_runner, grid)
#         right_delta = delta_right(curr_runner, grid)
#         update_runners = False
#         if down_delta < right_delta:
#             if curr_runner.pos[1] + 1 <= n - 1:
#                 clone_runner = curr_runner.__deepcopy__()
#                 clone_runner.go_right(right_delta)
#                 update_runners = True
#             curr_runner.go_down(down_delta)
#         else:
#             if curr_runner.pos[0] + 1 <= m - 1:
#                 clone_runner = curr_runner.__deepcopy__()
#                 clone_runner.go_down(down_delta)
#                 update_runners = True
#             curr_runner.go_right(right_delta)
#         if update_runners: update_all_runners(clone_runner, all_runners)
#     return curr_runner


# if __name__ == '__main__':
#     TR(
#         (
#             T(
#                 case=[
#                     [1,3,1],
#                     [1,5,1],
#                     [4,2,1],
#                 ], 
#                 expected=7,
#             ),
            # T(
            #     case=[
            #         [1, 2, 5, 6],
            #         [1, 3, 2, 3],
            #         [2, 3, 2, 1],
            #         [2, 1, 5, 1],
            #     ], 
            #     expected=11,
            # ),
            # T(
            #     case=[
            #         [1,1,1],
            #         [1,1,1],
            #         [1,1,1]
            #     ],
            #     expected=5,
            # ),
            # T(
            #     case=[
            #         [1,1,1],
            #         [2,2,2],
            #     ],
            #     expected=5,
            # ),
            # T(
            #     case=[
            #         [10,1],
            #         [10,2],
            #         [1,300],
            #         [1,1]
            #     ],
            #     expected=23,
            # ),
    #         T(
    #             case=[
    #                 [1,4,8,6,2,2,1,7],
    #                 [4,7,3,1,4,5,5,1],
    #                 [8,8,2,1,1,8,0,1],
    #                 [8,9,2,9,8,0,8,9],
    #                 [5,7,5,7,1,8,5,5],
    #                 [7,0,9,4,5,6,5,6],
    #                 [4,9,9,7,9,1,9,0]
    #             ],
    #             expected=47,
    #         ),
    #     ),
    #     min_path_sum
    # )()
