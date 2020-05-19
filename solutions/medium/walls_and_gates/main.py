from typing import List


class Solution:    
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        more_to_fill = True  # tracks if there are still more infinities that I need to fill

        m, cols = len(rooms), len(rooms[0])
        MAX = 2 ** 31 - 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def fill(rooms: List[List[int]]) -> bool:
            more = False
            # try to fill as many blocks as possible
            for row in range(m):
                for col in range(cols):
                    min_ = MAX

                    for d in directions:
                        row_direction = row + d[0]
                        col_direction = col + d[1]

                        if (row_direction >= 0 and row_direction < m) and (col_direction >= 0 and col_direction < cols):
                            val = rooms[row_direction][col_direction]

                        if val == -1:
                            continue

                        if val >= 0 and val != MAX:
                            min_ = min(min_, val)
                        else:
                            more = True

                    if min_ >= 0 and min_ != MAX and rooms[row][col] != 0:
                        rooms[row][col] = min_ + 1
            return more

        while more_to_fill: more_to_fill = fill(rooms)
        return


if __name__ == '__main__':
    Solution().wallsAndGates(
        [
          [1, 1, 0, 2147483647],
          [0, 1, 1, -1],
          [1, 2, 2, -1],
          [0, -1, 2147483647, 2147483647]
        ]
    )
    ...