#!/usr/bin/env python
from solutions.minions import Tree
from typing import List


def build_tree(preorder: List[int], inorder: List[int]) -> Tree:
    pre_idx = 0  # peek one by one off the preorder list
    idx_map = { val: ix for ix, val in enumerate(inorder) }

    def helper(in_left = 0, in_right = len(inorder)):
        nonlocal pre_idx
        if in_left == in_right:
            return None
        root_val = preorder[pre_idx]
        root = Tree(root_val)
        index = idx_map[root_val]
        pre_idx += 1
        root.left = helper(in_left, index)
        root.right = helper(index + 1, in_right)
        return root

    # def builder(in_left: int = 0, in_right: int = len(inorder)):
    #     nonlocal pre_ix
    #     val = preorder[pre_ix]
    #     pre_ix += 1
    #     root = Tree(val)
    #     ix = in_val_ix[val]
    #     root.left  = builder()
    #     root.right = builder()
    #     return root

    return helper()


if __name__ == '__main__':
    print(build_tree([9], [9]))
