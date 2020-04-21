#!/usr/bin/env python
from typing import List

from solutions.minions import Tree


# Time  O(N * logN). For each val need to find where to insert it
# Space O(N)
class Solution(object):
    def bstFromPreorder(self, preorder):
        res = None
        for x in preorder:
            res = self.insertIntoBST(res, x)
        return res

    def insertIntoBST(self, root, val):
        if root == None:
            return Tree(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

# def insert_into_tree(
#     val: int, tree: Tree, side: str = '', prev_tree: Tree = None
# ):
#     if tree is None: 
#         if side == 'left':
#             prev_tree.left = val
#             return
#         else:
#             prev_tree.right = val
#             return

#     if val < tree.val:
#         insert_into_tree(val, tree.left, 'left', tree)
#     # val > tree.val. condition that all the values are unique
#     else:
#         insert_into_tree(val, tree.right, 'right', tree)


# def bst_from_preorder(preorder: List[int]) -> Tree:
#     root = Tree(preorder[0])
#     for i in range(1, len(preorder)): insert_into_tree(preorder[i])
#     return root


if __name__ == '__main__':
    ...
