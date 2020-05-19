#!/usr/bin/env python
from typing import Optional, Tuple

from solutions.minions import Tree


class Solution:
    def traverse_find(
        self,
        root: Optional[Tree],
        target: int,
        *,
        depth: int = 0,
        parent: Tree,
    ) -> Tuple[int, Tree]:
        if root is None:
            return -1, Tree(-1)

        if root.v == target: return depth, parent

        depth_1, parent_1 = self.traverse_find(root.left,  target, depth=depth + 1, parent=root)
        depth_2, parent_2 = self.traverse_find(root.right, target, depth=depth + 1, parent=root)

        if depth_1 > depth_2:
            return depth_1, parent_1
        else:
            return depth_2, parent_2


    # get the depth of x, get the depth of y
    # if both are on the same depth AND parents different = cousins
    def isCousins(self, root: Tree, x: int, y: int) -> bool:
        depth_x, parent_x = self.traverse_find(root, x, parent = Tree(-1))  # sentinel parent
        depth_y, parent_y = self.traverse_find(root, y, parent = Tree(-1))  # sentinel parent
        return parent_x != parent_y and depth_x == depth_y


if __name__ == "__main__":
    t = Tree(1, Tree(2, None, Tree(4)), Tree(3))
    s = Solution()
    s.isCousins(t, 2, 3)
    ...