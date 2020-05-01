#!/usr/bin/env python
from solutions.minions import Tree


# ! S=O(N) number of nodes are stored in the recursion stack frames. average case though is O(H) height of the tree
# T = O(N)
def tree_diamter(t: Tree):
    num_of_nodes = 0
    def depth(t: Tree):
        nonlocal num_of_nodes
        if t is None: return 0
        L = depth(t.left)
        R = depth(t.right)
        num_of_nodes = max(num_of_nodes, L + R)
        return max(L, R) + 1
    depth()
    return num_of_nodes


if __name__ == '__main__':
    print(tree_diamter(Tree(1, Tree(2, Tree(4)), Tree(3))))
