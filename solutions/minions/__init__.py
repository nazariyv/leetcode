from typing import TypeVar, Optional, List, Dict, Any, Callable, Iterable, Sequence, Generic
from sortedcontainers import SortedList
from collections import namedtuple
import logging
import os

os.system("")
TestCase = namedtuple("TestCase", ["case", "expected"])


log = logging.getLogger("minions")
T = TypeVar('T')
Out = TypeVar('Out')
In = TypeVar('In')


class Stack(Generic[T]):
    __slots__ = 'stack'
    def __init__(self) -> None:
        self.stack: List[T] = []
    def push(self, x: T) -> None:
        self.stack.append(x)
    def pop(self) -> Optional[T]:
        popped = None
        if self.stack: popped = self.stack.pop()
        return popped
    def top(self) -> Optional[T]:
        topof = None
        if self.stack: topof = self.stack[-1]
        return topof
    def __len__(self) -> int: return len(self.stack)


class Queue(Generic[T]):
    __slots__ = ('_queue', '_head', '_tail')

    def __init__(self) -> None:
        self._queue: List[T] = []
        self._head: Optional[T] = None
        self._tail: Optional[T] = None

    def enqueue(self, x: T) -> None:
        self._queue.append(x)
        self._tail = self._queue[-1]

    def dequeue(self) -> Optional[T]:
        top = None
        if self._queue:
            top = self._queue[0]
            del self._queue[0]
        self._head = None if not self._queue else self._queue[0]
        return top

    @property
    def head(self) -> Optional[T]:
        return self._head

    @property
    def tail(self) -> Optional[T]:
        return self._tail


class Tree(Generic[T]):
    __slots__ = ('v', 'left', 'right')
    def __init__(self, v: T, left: 'Optional[Tree]' = None, right: 'Optional[Tree]' = None):
        self.v     = v
        self.left  = left
        self.right = right
    def repr(self, vals: Optional[List[T]] = None) -> str:
        if vals is None:
            vals = list()
        pre_ordered = self.pre_order()
        str_pre_ordered = [repr(x) for x in pre_ordered]
        return f'[{"|".join(str_pre_ordered)}]'
    def __repr__(self) -> str:
        return self.repr()
    def pre_order(self, vals: Optional[List[T]] = None) -> List[T]:
        if vals is None:
            vals = list()
        vals.append(self.v)
        if self.left is not None:
            vals.extend(self.left.pre_order())
        if self.right is not None:
            vals.extend(self.right.pre_order())
        return vals

    def in_order(self, vals: Optional[List[T]] = None) -> List[T]:
        if vals is None:
            vals = list()
        if self.left is not None:
            vals.extend(self.left.in_order())
        vals.append(self.v)
        if self.right is not None:
            vals.extend(self.right.in_order())
        return vals


class ListNode(Generic[T]):
    def __init__(self, x: Optional[T] = None, next: Optional['ListNode'] = None):
        self.val = x
        self.next = next
    def __repr__(self) -> str:
        stack = [str(self.val)]
        next_ = self.next
        while next_ is not None:
            stack.append(str(next_.val))
            next_ = next_.next
        return "->".join(stack)
    def __eq__(self, other: Any) -> bool:
        curr_self: Optional['ListNode'] = self
        curr_other = other
        while curr_self is not None and curr_other is not None:
            if curr_self.val != curr_other.val: return False
            if curr_self.next is None and curr_other.next is not None: return False
            if curr_self.next is not None and curr_other.next is None: return False
            curr_self  = curr_self.next
            curr_other = curr_other.next
        return True
    def __hash__(self) -> int:
        curr_self: Optional['ListNode'] = self
        stack = []
        while curr_self is not None:
            stack.append(curr_self.val)
            curr_self = curr_self.next
        return hash(tuple(stack))


def curry(func: Callable) -> Callable:
    def curried(*args: Any, **kwargs: Any) -> Any:
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


def verbose(func: Callable) -> Callable:
    def verbosed(*args: Any, **kwargs: Any) -> Any:
        r = func(*args, **kwargs)
        log.debug(f"""\
called {func.__module__}.{func.__name__} with args: {args}, \
kwargs: {kwargs}, which outputted: {r}""")
        return r
    return verbosed

class Style:
    class Descriptor:
        RESET = '\033[0m'
        @classmethod
        def d(cls, color: str) -> Callable[[str], str]: return lambda s: f"{color}{s}{cls.RESET}"

    descriptor = Descriptor.d

    BLACK     = descriptor('\033[30m')
    RED       = descriptor('\033[31m')
    GREEN     = descriptor('\033[32m')
    YELLOW    = descriptor('\033[33m')
    BLUE      = descriptor('\033[34m')
    MAGENTA   = descriptor('\033[35m')
    CYAN      = descriptor('\033[36m')
    WHITE     = descriptor('\033[37m')
    UNDERLINE = descriptor('\033[4m')


def iterable_comparator(x: Sequence, y: Sequence) -> bool:
    x = SortedList(x)
    y = SortedList(y)
    if len(x) != len(y):
        return False
    for i, j in zip(x, y):
        if i != j: return False
    return True


class TestRunner:
    def __init__(self, test_cases: Iterable[TestCase], runner: Callable[[In], Out], comparator: Optional[Callable] = None):
        self.test_cases = test_cases
        self.runner = runner
        self.comparator = comparator

    def __call__(self) -> None:
        for test in self.test_cases:
            log.debug(Style.YELLOW(f"commencing test case: {test} for {self.runner.__name__}"))
            actual = self.runner(test.case)
            equal = self.comparator(test.expected, actual) if self.comparator is not None else test.expected == actual
            styler = Style.GREEN if equal else Style.RED
            log.info(styler(f"expected:{test.expected},actual:{actual},test:{test.case}"))


def bisect_left(sorted_arr: List[int], target: int) -> int:
    lo, hi = 0, len(sorted_arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if (sorted_arr[mid] > target): hi = mid
        else:                 lo = mid + 1
    return lo


def find_index(l: List[T], target: T) -> int:
    try:
        return l.index(target)
    except IndexError:
        return -1
