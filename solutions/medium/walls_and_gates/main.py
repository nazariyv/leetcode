from typing import List, MutableSequence, Tuple
from collections import deque


INF = 2 ** 31 - 1


class Solution:
    def identify_all_gates(self, rooms: List[List[int]], m: int, n: int) -> List[Tuple[int, int, int]]:
        res: List[Tuple[int, int, int]] = []
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == 0: res.append((row, col, 0,))
        return res

    def wallsAndGates(self, rooms: List[List[int]]) -> List[List[int]]:
        # I may traverse the ones that I have already traversed, to avoid this
        # \ simply traverse it ONLY IF the new cost is LOWER than the assigned one
        # \ else do not traverse
        # First loop to find all gates.
        # Next, start breadth first search from each gate (meaning look at all neighbouts)
        # \ with a queue
        # Once the queue is empty, you are done

        # time cost is O(nm) for first loop to identify all the gates
        # then need to traverse all of them again to determine the 
        # path length to the nearest gate, this is O(nm) again
        # So all in all this is O(2 * nm) = O(nm)
        m = len(rooms)
        n = len(rooms[0])

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1),)
        all_gates_prelim = self.identify_all_gates(rooms, m, n)
        all_gates: deque = deque()
        for gate in all_gates_prelim: all_gates.append(gate)

        try:
            while node := all_gates.popleft():
                for d in directions:
                    if 0 <= node[0] + d[0] < m and 0 <= node[1] + d[1] < n:
                        # if visited, then only add if current +1 at the new node is less than the current value
                        print(node[0] + d[0], node[1] + d[1])
                        neighbour_val = rooms[node[0] + d[0]][node[1] + d[1]]
                        if neighbour_val > 0 and neighbour_val != INF and neighbour_val != -1:
                            if rooms[node[0] + d[0]][node[1] + d[1]] > node[2] + 1:
                                rooms[node[0] + d[0]][node[1] + d[1]] = node[2] + 1
                                all_gates.append((node[0] + d[0], node[1] + d[1], node[2] + 1,))
                        # not visited
                        elif rooms[node[0] + d[0]][node[1] + d[1]] == INF:
                            rooms[node[0] + d[0]][node[1] + d[1]] = node[2] + 1
                            all_gates.append((node[0] + d[0], node[1] + d[1], node[2] + 1,))
        except IndexError:
            pass

        return rooms


if __name__ == '__main__':
    rms = Solution().wallsAndGates(
        [
          [INF, INF, 0,   INF],
          [0,   INF, INF,  -1],
          [INF, INF, INF,  -1],
          [0,   -1,  INF, INF]
        ]
    )
    ...