#!/usr/bin/env python
from collections import deque, namedtuple
StackNode = namedtuple('StackNode', ['value', 'min'])

# We are pushing items into the main stack
# We have second stack to contain unique min elements without repetition
# Our goal is to return the global minimum from the second stack
# It is true that when the last reference to a min in the second stack is removed
# that min is no longer global and should be removed

class MinStack:
    def __init__(self): self.stack, self.min_stack = [], []
    def push(self, x: int) -> None:
        # We always put the number onto the main stack.
        self.stack.append(x)
        # If the min stack is empty, or this number is smaller than
        # the top of the min stack, put it on with a count of 1.
        if not self.min_stack or x < self.min_stack[-1][0]: self.min_stack.append([x, 1])
        # Else if this number is equal to what's currently at the top
        # of the min stack, then increment the count at the top by 1.
        elif x == self.min_stack[-1][0]: self.min_stack[-1][1] += 1

    def pop(self) -> None:
        # If the top of min stack is the same as the top of stack
        # then we need to decrement the count at the top by 1.
        if self.min_stack[-1][0] == self.stack[-1]: self.min_stack[-1][1] -= 1
        # If the count at the top of min stack is now 0, then remove
        # that value as we're done with it.
        if self.min_stack[-1][1] == 0: self.min_stack.pop()
        # And like before, pop the top of the main stack.
        self.stack.pop()

    def top(self) -> int:    return self.stack[-1]
    def getMin(self) -> int: return self.min_stack[-1][0]

# ALWAYS LOOK FOR INVARIANTS WHEN SOLVING THE PROBLEMS
# class MinStack:
#     # Goal: do not repeat myself with the minimum values
#     # Thoughts: need each value in the original stack to point to its minimum value when it is removed from the stack
#     # Idea 1: use dict. Have non repeating minimum values as keys and which stack nodes they correspond to as values
#     # this is bad, because I would need to traverse the value, which is O(n)
#     # Idea 2: have two stacks alongside each other. The main stack will have pointers to the second stack that
#     # will contain non repeating minimum values. Whenever there is a new a min, that is not at the top of the 
#     # second stack, we push it to the second stack. How do we determine when to pop the minimum from the second
#     # stack? When the value from the main stack == the value to which it points in the second stack and we remove
#     # it from the main stack, then that is when we remove the value from the second stack too.
#     # [0, 2, -1, 3]
#     # [0, -1]
#     # This algorithm will have a better O(n) space complexity than the one below
#     def __init__(self): self.stack, self.min_stack = [], []
#     def push(self, x: int) -> None:
#         if self.min_stack and x < self.min_stack[-1]: self.min_stack.append(x)
#         elif not self.min_stack:                      self.min_stack.append(x)
#         # call by object (not call by object-reference), we are not creating a reference here, but merely copying a value!
#         self.stack.append((x, self.min_stack[-1],))
#     def pop(self) -> None:
#         poop = self.stack.pop()
#         # ? is it possible for it to still point to the wrong min stack even after this  remove?
#         if self.stack and self.min_stack:
#             if self.stack[-1][1] != self.min_stack[-1]: self.min_stack.pop()
#         elif not self.stack and self.min_stack:
#             self.min_stack.pop()
#         else:  # self.stack and not self.min_stack:
#             raise Exception("unknown case")
#     def top(self) -> int:
#         return self.stack[-1][0] if self.stack else -1
#     def getMin(self) -> int:
#         return self.min_stack[-1] if self.min_stack else -1
#     def __repr__(self):      return f"stack:{self.stack}\nmin_stack{self.min_stack}"

# this solution requires O(2 * n) = O(n) space
# some of the minimums repeat themselves, and so it is not great
# class MinStack:
#     def __init__(self):
#         self.global_min = float('inf')
#         self.stack      = []
#     def push(self, x: int) -> None:
#         self.stack.append(StackNode(value=x, min=self.global_min))
#         self.global_min = min(x, self.global_min)
#     def pop(self) -> None:
#         r = self.stack.pop()
#         self.global_min = r.min
#         return
#     def top(self) -> int:
#         if self.stack: return stack[-1].value
#     def getMin(self) -> int:
#         return self.global_min


# not correct because uses the implementation already
# class MinStack:
#     # if I use list to model stack, then .pop(0) will take O(n) time
#     # I can use deque, which is a queue object, which uses doubly linked list structure
#     # to achieve O(1) insert at both ends, as well as remove O(1) at both ends
#     def __init__(self):
#         self.global_min = float('inf')  # no min at start
#         self.d = deque()
#     def push(self, x: int) -> None:
#         self.d.append(StackNode(value=x, min=self.global_min))
#         self.global_min = min(x, self.global_min)
#     def pop(self) -> None:
#         r = self.d.pop()
#         self.global_min = r.min
#     def top(self) -> int:
#         if self.d: return self.d[-1].value
#     def getMin(self) -> int: return self.global_min


# the question is equivalent to that of maintaining a minimum of a stack in constant time O_O
# [-2,-3,0,]
if __name__ == '__main__':
    minStack = MinStack()
    # exepcted = [null,null,null,null,-3,null,0,-2]
    # minStack.push(-2)
    # minStack.push(0)
    # minStack.push(-3)
    # print(minStack)
    # print(f"min:{minStack.getMin()}")
    # minStack.pop()
    # print(minStack)
    # print(f"top:{minStack.top()}")
    # print(f"min:{minStack.getMin()}")

    # ["MinStack","push","push","push","push","getMin","pop","getMin","pop","getMin","pop","getMin"]
    # [[],[2],[0],[3],[0],[],[],[],[],[],[],[]]
    # expected [null,null,null,null,null,0,null,0,null,0,null,2]
    # actual   [null,null,null,null,None,0,None,3, 3,  0,     2]

    # minStack.push(2) # SN(v=2,min=2) global=2
    # minStack.push(0) # SN(v=0,min=2) global=0
    # minStack.push(3) # SN(v=3,min=0) global=0
    # minStack.push(0) # SN(v=0,min=0) global=0
    # print(minStack)
    # print(minStack.getMin())
    # minStack.pop()
    # print(minStack)
    # print(minStack.getMin())
    # minStack.pop()
    # print(minStack)
    # print(minStack.getMin())
    # minStack.pop()
    # print(minStack)
    # print(minStack.getMin())

    # ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
    # [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]

    print(minStack)
    minStack.push(2147483646)
    print(minStack)
    minStack.push(2147483646)
    print(minStack)
    minStack.push(2147483647)
    print(minStack)
    minStack.top()
    print(minStack)
    minStack.pop()
    print(minStack)
    minStack.getMin()
    print(minStack)
    minStack.pop()
    print(minStack)
    minStack.getMin()
    print(minStack)
    minStack.pop()
    print(minStack)
    minStack.push(-2147483648)
    print(minStack)
    minStack.top()
    print(minStack)
    minStack.getMin()
    print(minStack)
    minStack.pop()
    print(minStack)
    minStack.getMin()
