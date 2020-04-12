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
