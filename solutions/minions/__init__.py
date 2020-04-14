from typing import TypeVar, Optional
T = TypeVar('T')


class Stack:
    def __init__(self):           self.stack = []
    def push(self, x: T):         self.stack.append(x)
    def pop(self) -> Optional[T]:
        popped = None
        if self.stack: popped = self.stack.pop()
        return popped
    def top(self) -> Optional[T]:
        topof = None
        if self.stack: topof = self.stack[-1]
        return topof
    def __len__(self) -> int: return len(self.stack)


class Tree:
    def __init__(self, v: T, left: 'Optional[Tree]' = None, right: 'Optional[Tree]' = None):
        self.v     = v
        self.left  = left
        self.right = right


def curry(func):
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return (
                lambda *args2, **kwargs2:
                    curried(
                        *(args + args2),
                        **dict(kwargs, **kwargs2)
                    )
            )
    return curried
