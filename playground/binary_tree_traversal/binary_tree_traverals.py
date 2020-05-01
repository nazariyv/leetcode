#!/usr/bin/env python
from solutions.minions import Tree
from typing import List

# Breadth First Search
# You move each level at a time
# all the children of the current level nodes are printed left to right


# --------------------- BREADTH FIRST SEARCHES ------------------------
bfs_tree = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3))

def breadth_first_search(tree: Tree, prev_children: List[Tree] = None) -> None:
    if prev_children is None: print(tree.v)
    immediate_children = []
    if prev_children:
        for child in prev_children:
            if child is not None:
                print(child.v)
                immediate_children.append(child.left)
                immediate_children.append(child.right)
    else:
        immediate_children = [tree.left, tree.right]
    # ! this check is very inefficient
    if all(x is None for x in immediate_children): return
    return breadth_first_search(tree, immediate_children)


# ----------------------- DEPTH FIRST SEARCHES --------------------------
# you traverse down as far as possible. However, the order in which you print
# varies between the below three

post_tree = Tree(5, Tree(3, Tree(1), Tree(2)), Tree(4))
def postorder(t: Tree) -> None:
    """bottom to top. print lefts to right then self"""
    if t is None: return
    postorder(t.left)
    postorder(t.right)
    print(t.v)

inorder_tree = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(5))
def inorder(t: Tree) -> None:
    """bottom to top. print left. print self. print right"""
    if t is None: return
    inorder(t.left)
    print(t.v)
    inorder(t.right)

preorder_tree = Tree(1, Tree(2, Tree(3), Tree(4)), Tree(5))
def preorder(t: Tree) -> None:
    """bottom to top. print self. print left. print rignt.
    """
    if t is None: return
    print(t.v)
    preorder(t.left)
    preorder(t.right)


if __name__ == '__main__':
    print("---- BFS ----")
    breadth_first_search(bfs_tree)
    print("--------")
    print("----- POSTORDER -----")
    postorder(post_tree)
    print("---- INORDER -----")
    inorder(inorder_tree)
    print("------ PREORDER -------")
    preorder(preorder_tree)
