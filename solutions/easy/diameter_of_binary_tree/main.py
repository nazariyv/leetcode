#!/usr/bin/env python
from typing import Callable, Iterable, Optional

from solutions.minions import Tree
Specifier = Callable[[Tree], bool]

# Features (over-engineered items):
# 1. Decorators
# 2. Currying
# 3. Recursion


def curry(func):
    def curried(*args, **kwargs):
        if 'tree' in kwargs:
            return func(*args, **kwargs)
        return (
                lambda *args2, **kwargs2:
                    curried(
                        *(args + args2),
                        **dict(kwargs, **kwargs2)
                    )
            )
    return curried

class BranchSpecifiers:
    @staticmethod
    def is_a_mountain(tree: Tree) -> int:
        if (
            all(
                branch is None for branch in
                (
                    tree.left.left,
                    tree.left.right,
                    tree.right.left,
                    tree.right.right,
                )
            )
        ): return 2
        return -1

    @staticmethod
    def is_lonely(tree: Tree) -> int:
        nil_tree_left, nil_tree_right = tree.left is None, tree.right is None
        if not any(
            (
                nil_tree_left  and not nil_tree_right,
                nil_tree_right and not nil_tree_left,
            )
        ): return -1
        traverse_this = tree.left if nil_tree_right  else tree.right
        if all(
            (
                traverse_this.left is None,
                traverse_this.right is None,
            )
        ): return 1
        return -1

    is_very_lonely: Callable[[Tree], int] = staticmethod(
        (lambda tree: 0 if all(
            (tree.left is None, tree.right is None,)
        ) else -1)
    )
    is_nil: Callable[[Tree], int] = staticmethod((lambda tree: 0 if tree is None else -1))


# no conditions to check if the first arg is tree, careful not to pass specifier first
# for better performance pass the easier specifiers first (e.g. is_non_existent)
@curry
def branch_length(*specifiers: Iterable[Specifier], tree: Optional[Tree] = None):
    for specifier in specifiers:
        path_length = specifier(tree)
        if path_length > -1: return path_length
    return -1



def longest_path(tree: Tree):
    longest = 0
    bs = BranchSpecifiers
    branch_specifiers = branch_length(bs.is_nil)(bs.is_very_lonely)(bs.is_lonely)(bs.is_a_mountain)
    # while tree.left or tree.right:
    left_length, right_length   = 0, 0
    if tree.left:  left_length  = branch_specifiers(tree=tree.left)
    if tree.right: right_length = branch_specifiers(tree=tree.right)
    longest = max(longest, left_length, right_length, )
    return longest

def tree_diameter(tree: Tree): return longest_path(tree)


if __name__ == '__main__':
    mountain = Tree(1, left=Tree(2), right=Tree(3))
    right_lonely = Tree(1, left=Tree(2))
    left_lonely = Tree(1, right=Tree(2))
    not_a_tree = None
    # print(is_a_mountain(mountain))
    # print(is_a_mountain(left_lonely))
    # print(is_a_mountain(right_lonely))
    # print(is_non_existent(not_a_tree))
    # print(is_lonely(mountain))
    # print(is_lonely(left_lonely))
    # print(is_lonely(right_lonely))
    # print(is_lonely(not_a_tree))
    # print(is_non_existent(mountain))
    # print(is_non_existent(left_lonely))
    # print(is_non_existent(right_lonely))
    # print(is_non_existent(not_a_tree))
    bs = BranchSpecifiers
    branch_specifiers = branch_length(bs.is_nil)(bs.is_very_lonely)(bs.is_lonely)(bs.is_a_mountain)

    print(branch_specifiers(tree=mountain))
    print(branch_specifiers(tree=left_lonely))
    print(branch_specifiers(tree=right_lonely))
    print(branch_specifiers(tree=not_a_tree))

    print(longest_path(mountain))
