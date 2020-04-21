#!/usr/bin/env python
from solutions.minions import TestCase as T, TestRunner as TR, Tree
from typing import List, Dict, Any


# class FakeTree(Tree):
#     def __init__(self, val, left, right, fake):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.fake = fake


def construct_branch(preorder: List[int]) -> List[List[int]]:
    n = len(preorder)
    out = []
    if n == 0: return out
    if n == 1: return [preorder[0], out]
    curr, next = preorder[0], None
    out = [[curr, []]]
    curr_ix = 0
    for i in range(1, n):
        next = preorder[i]
        if curr > next: out[curr_ix][1].append(next)
        else:
            curr = next
            curr_ix += 1
            out.append([next, []])
    for ix, item in enumerate(out): out[ix][1] = construct_branch(item[1])
    return out

def make_tree(happy_tree) -> Tree:
    if isinstance(happy_tree[0], int): return Tree(happy_tree[0])
    branches = happy_tree[0][1]
    root = Tree(happy_tree[0][0])
    prev = root
    for ix, branch in enumerate(happy_tree):
        lefts = branch[1]
        if lefts:
            prev.left = make_tree(lefts)
        if ix == 0: continue
        t = Tree(branch[0])
        prev.right = t
        prev = t
    return root

# I will implement T=O(log_2(N)), S=O(N)
# another solution I could think of is T=O(N ** 2) and S=O(1)
def bst_from_preorder(self, preorder: List[int]) -> TreeNode:
    happy_tree = construct_branch(preorder)
    root = make_tree(happy_tree)
    return root


if __name__ == '__main__':
    TR(
        (
            T(),
            T(),
            T(),
            T(),
            T(),
        ),
        bst_from_preorder,
    )()
