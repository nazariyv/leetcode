#!/usr/bin/env python
from typing import List

from solutions.minions import Tree as TreeNode


# recursive
def preorderTraversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    res = []
    res.append(root.val)
    res += preorderTraversal(root.left)
    res += preorderTraversal(root.right)
    return res


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # DFS
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node: continue
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return res


if __name__ == '__main__':
    Solution().preorderTraversal(TreeNode(1, TreeNode(2), TreeNode(3)))
    ...