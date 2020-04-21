# #!/usr/bin/env python
# from typing import List, Generator, Tuple
# from sortedcontainers import SortedList
# from solutions.minions import Style
# import logging
# log = logging.getLogger("minmum_path_sum")

# class Runner:
#     pos: List[int]  # Tuple[int, int]
#     cost: int
#     cheapest_next_move: Runner

# def go_down(r: Runner, cost: int):
#     r.pos[0] = r.pos[0] + 1
#     r.cost += cost

# def go_right(r: Runner, cost: int):
#     r.pos[1] = r.pos[1] + 1
#     r.cost += cost

# # given a function that will calculate the cheapest path for each runner
# # how will it help?
# # at each step, if the cheapest next move has not been computed
# # we will know which runner to proceed

# def min_path_sum(grid: List[List[int]]) -> int:
#     # TODO index issues
#     m = len(grid)
#     n = len(grid[0])
#     min_runner  = Runner([0, 0], 0)
#     all_runners = SortedList(key=lambda x: x.cost)

#     # ? what is missing ?
#     # * logic to determine the min runner
#     # * logic to store all the runners
#     # TODO: index issues
#     while min_runner.pos[0] != m - 1 and min_runner.pos[1] != n - 1:
#         down_marginal_cost  = grid[min_runner.pos[0] + 1, min_runner.pos[1]]
#         right_marginal_cost = grid[min_runner.pos[0], min_runner.pos[1] + 1]

#         runner_clone = Runner(min_runner.pos, min_runner.cost)

#         if down_marginal_cost < right_marginal_cost:
#             go_down(min_runner)
#             go_right(runner_clone)
#         else:
#             go_right(min_runner)
#             go_down(runner_clone)

#     return min_runner.cost



# # [
# #   [1,3,1],
# #   [1,5,1],
# #   [4,2,1]
# # ]

# [1,1,2,3,2,2,1]
# [2,3,1,1,4,5,1]
# [2,1,1,3,4,5,5]
# [6,6,6,6,7,7,8]
# [1,1,1,1,1,1,1]















# if __name__ == '__main__':
#     tests = {

#     }
#     for test, expected in tests.items():
#         actual = min_path_sum(test)
#         styler = Style.GREEN if actual == expected else Style.RED
#         log.info(styler(f"actual:{actual},expected:{expected},test:{test}"))
