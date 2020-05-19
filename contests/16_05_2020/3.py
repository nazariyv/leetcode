#!/usr/bin/env python
from typing import Optional, List
from copy import deepcopy as dc

from solutions.minions import Tree as TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def preorder(t: Optional[TreeNode], lst: Optional[List[int]] = None) -> None:
            nonlocal ans

            if t:
                if lst is None: lst = []
                if lst and t.v >= max(lst): ans += 1
                lst.extend([t.v])
                preorder(t.left,  lst=dc(lst))
                preorder(t.right, lst=dc(lst))

        preorder(root)

        return ans + 1


if __name__ == '__main__':
    Solution().goodNodes(
        TreeNode(
            2,
            None,
            TreeNode(
                4,
                TreeNode(10),
                TreeNode(
                    8,
                    TreeNode(4)
                )
            )
        )
    )
    ...
