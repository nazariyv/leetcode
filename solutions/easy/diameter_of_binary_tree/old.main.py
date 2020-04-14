#!/usr/bin/env python
from typing import Optional

class Tree:...
class Tree:
    def __init__(self, val: int, left: Optional[Tree] = None, right: Optional[Tree] = None):
        self.val   = val
        self.left  = left
        self.right = right


# each node has to be treated as a tree and for each node we need to compute the max_depth
# and keep track of the global value
# instead of returning the max of either the left or right path, I should return the max path for each node
# and then in the end it will the max path
def tree_diamter(tree: Tree, curr_depth: int = 0, max_path: int = 0):
    if tree.left is None and tree.right is None:
        return max_path
    l, r = 0, 0
    if tree.left:
        l = tree_diamter(tree.left,  curr_depth + 1, max(curr_depth + 1, max_path))
    if tree.right:
        r = tree_diamter(tree.right, curr_depth + 1, max(curr_depth + 1, max_path))
    return max(l, r, max_path)


if __name__ == '__main__':
    # t = Tree(1, left=Tree(2, left=Tree(4)), right=Tree(3))
    # t = Tree(1, left=Tree(2, left=Tree(4), right=Tree(5)), right=Tree(3))
    # t = Tree(1, right=Tree(3, right=Tree(4)))
    t1 = Tree(
        6,
        left=Tree(0,  right=Tree(-1)),
        right=Tree(6, left=Tree(-4)),
    )

    t2 = Tree(
            -3,
            left=Tree(
                -9,
                left=Tree(
                    9,
                    left=t1
                ),
                right=Tree(
                    -7,
                    left=Tree(-6,  left=Tree(5)),
                    right=Tree(-6, left=Tree(9, left=Tree(-2))),
                ),
            ),
            right=Tree(
                -3,
                left=Tree(
                    -4
                ),
            ),
        )

    t3 = Tree(4,
        left=Tree(
            -7
        ),
        right=t1
    )
    print(tree_diamter(Tree(9, left=t1)))
    # print(r)
