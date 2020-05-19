#!/usr/bin/env python
from typing import Optional
from solutions.minions import Tree


# ! S=O(N) number of nodes are stored in the recursion stack frames. average case though is O(H) height of the tree
# T = O(N)
def tree_diamter(t: Tree) -> int:
    ans = 0

    def depth(t: Optional[Tree]) -> int:
        nonlocal ans

        if t is None: return 0

        L = depth(t.left)
        R = depth(t.right)

        ans = max(ans, L + R)

        return max(L, R) + 1

    return depth(t)


if __name__ == '__main__':
    print(tree_diamter(Tree(1, Tree(2), Tree(3))))
