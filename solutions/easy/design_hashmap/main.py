#!/usr/bin/env python
from collections import namedtuple
from typing import Optional


Key_Val = namedtuple('Key_Val', ['key', 'val'])


class LinkedList:
    def __init__(self, v: Optional[Key_Val] = None, nxt: Optional['LinkedList'] = None):
        self.v = v
        self.nxt = nxt

    def get(self, k: int) -> int:
        nxt = self
        while nxt is not None:
            if nxt.v is not None:
                if nxt.v.key == k:
                    return nxt.v.val
            nxt = nxt.nxt
        return -1

    def put(self, k: int, v: int) -> None:
        prev = LinkedList(Key_Val(-1, 0))
        curr = self
        insert_this = Key_Val(k, v)
        if self.v is None: self.v = insert_this; return
        while curr is not None:
            if curr.v is not None:
                if curr.v.key == k: curr.v = insert_this; return
                prev = curr
                curr = curr.nxt
        if prev.key != -1: prev.nxt = LinkedList(Key_Val(k, v))

    def delete(self, k: int) -> None:
        while self is not None and self.v is not None and self.v.key == k:
            self.v = None
            return

        prev = self
        curr = self.nxt
        head = prev

        while curr is not None:
            if curr.v is not None:
                if curr.v.key == k: prev.nxt = curr.nxt
                else:               prev = curr
            curr = curr.nxt

        self = head
        return


class MyHashMap:
    def __init__(self):
        self.p = 2069
        self.container = [LinkedList() for i in range(self.p)]

    def put(self, key: int, value: int) -> None:
        key_hash = key % self.p
        self.container[key_hash].put(key, value)

    def get(self, key: int) -> int:
        key_hash = key % self.p
        return self.container[key_hash].get(key)

    def remove(self, key: int) -> None:
        key_hash = key % self.p
        self.container[key_hash].delete(key)


if __name__ == "__main__":
    hm = MyHashMap()
    hm.put(1,1)
    hm.put(2,2)
    hm.get(1)
    hm.get(3)
    hm.put(2,1)
    hm.get(2)
    hm.remove(2)
    hm.get(2)

