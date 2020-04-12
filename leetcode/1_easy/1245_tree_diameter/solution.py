from typing import List
import timeit

class Solution:
    u_to_v = {}        # contains all the nodes and to what other nodes they are connected
    start_at_u_longest_path = {}  # contains each node and the longest path from that node

    def treeDiameter(self, edges: List[List[int]]) -> int:
        self.u_to_v = {}
        self.start_at_u_longest_path = {}

        for node_u, node_v in edges:
            if node_u in self.u_to_v:
                self.u_to_v[node_u].append(node_v)
            else:
                self.u_to_v[node_u] = [node_v]
            if node_v in self.u_to_v:
                self.u_to_v[node_v].append(node_u)
            else:
                self.u_to_v[node_v] = [node_u]

        def find_longest_path_for_node(
            node: int,
            arrived_from_node, #: Union[int, None],
            path_length: int,
            original_node: int
        ):
            curr_original_node = self.start_at_u_longest_path[original_node] if original_node in self.start_at_u_longest_path else 0
            # the base case is that the only option to traverse to, is the previous node
            if self.u_to_v[node] == [arrived_from_node]:
                self.start_at_u_longest_path[original_node] = max(curr_original_node, path_length); return

            # if we have already determined the length of the path then add the length so far
            # the below is flawed. look at: [[0,1],[1,2],[0,3],[3,4],[2,5],[3,6]]
            if node in self.start_at_u_longest_path:
                self.start_at_u_longest_path[original_node] = max(curr_original_node, path_length + self.start_at_u_longest_path[node]); return

            for node_ in self.u_to_v[node]:
                if node_ != arrived_from_node:
                    find_longest_path_for_node(node_, node, path_length + 1, original_node=original_node) 

        for node in self.u_to_v.keys():
            find_longest_path_for_node(node, None, 0, original_node=node)

        return max(self.start_at_u_longest_path.values())

class DifferentSolution:
    max_length = 0
    all_nodes = {}

    def treeDiameter(self, edges: List[List[int]]) -> int:

        for edge in edges:
            node_u, node_v = edge

            if node_u not in self.all_nodes:
                self.all_nodes[node_u] = [node_v]
            else:
                self.all_nodes[node_u].append(node_v)

            if node_v not in self.all_nodes:
                self.all_nodes[node_v] = [node_u]
            else:
                self.all_nodes[node_v].append(node_u)

        def traverse(node_to: int, node_from: int, running_path_length: int) -> None:
            # forbid going back on itself
            self.max_length = max(running_path_length, self.max_length)

            for node_v in self.all_nodes[node_to]:
                if node_v != node_from:
                    traverse(node_v, node_to, running_path_length + 1)

        for node_u in self.all_nodes:
            for node_v in self.all_nodes[node_u]:
                traverse(node_v, node_u, 1)

        return self.max_length

class BFS:
    all_nodes = {}
    class Queue:
        def __init__(self):
            self.items = []
        def push(self, item):
            self.items.append(item)
        def pop(self):
            return self.items.pop()
    def initialize_nodes(self, edges: List[List[int]]) -> int:
        for edge in edges:
            node_u, node_v = edge

            if node_u not in self.all_nodes:
                self.all_nodes[node_u] = [node_v]
            else:
                self.all_nodes[node_u].append(node_v)

            if node_v not in self.all_nodes:
                self.all_nodes[node_v] = [node_u]
            else:
                self.all_nodes[node_v].append(node_u)

    def treeDiameter(self, edges: List[List[int]]) -> int:
        # perform bfs from every node
        self.initialize_nodes(edges)
        max_length = 0
        q = self.Queue()
        for start_node in self.all_nodes.keys():
            length = 0
            all_visited_nodes = set([start_node])
            q.push((length, start_node))
            while q.items:
                length, visited = q.pop()
                for node in self.all_nodes[visited]:
                    if node not in all_visited_nodes:
                        q.push((length + 1, node))
                        max_length = max(max_length, length + 1)
                        all_visited_nodes.add(node)
        return max_length

# print(Solution().treeDiameter([[0,1],[1,2],[0,3],[3,4],[2,5],[3,6]]))
# print(DifferentSolution().treeDiameter([[0,1],[1,2],[0,3],[3,4],[2,5],[3,6]]))
print(BFS().treeDiameter([[9,2], [2, 1], [2, 4], [4, 5], [2, 3], [1, 6], [6, 7], [6, 8], [1, 0]]))

# print(timeit.repeat("Solution().treeDiameter([[0,1], [1,2]])", "from __main__ import Solution", number=5))
# print(timeit.repeat("DifferentSolution().treeDiameter([[0,1], [1,2]])", "from __main__ import DifferentSolution", number=10))
# print(timeit.repeat("BFS().treeDiameter([[0,1],[1,2],[0,3],[3,4],[2,5],[3,6]])", "from __main__ import BFS", number=10))


# print(f"random reg graph: {nx.random_regular_graph(10, 100).edges}")