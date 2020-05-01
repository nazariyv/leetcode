#!/usr/bin/env python
from typing import Dict, List

PositiveInt = int

class DoublyLinkedNode:
    def __init__(self, key: PositiveInt, value: int) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: PositiveInt) -> None:
        self.size:     PositiveInt = 0
        self.capacity: PositiveInt = capacity
        self.head = DoublyLinkedNode(-1, -1)
        self.tail = DoublyLinkedNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache: Dict[int, DoublyLinkedNode] = dict()

    def __move_node_to_head(self, node: DoublyLinkedNode) -> None:
        pred = self.head
        succ = self.head.next
        succ.prev = node
        pred.next = node
        node.prev = pred
        node.next = succ

    def __remove_node_links(self, node: DoublyLinkedNode) -> None:
        pred = node.prev
        succ = node.next
        succ.prev = pred
        pred.next = succ
        node.prev = None
        node.next = None

    def __remove_tail(self) -> int:
        to_delete = self.tail.prev
        k = to_delete.key
        pred = to_delete.prev
        self.tail.prev = pred
        pred.next = self.tail
        del to_delete
        return k

    def get(self, key: PositiveInt) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self.__remove_node_links(node)
        self.__move_node_to_head(node)
        return node.value

    def put(self, key: PositiveInt, value: int) -> None:
        if key not in self.cache and self.size == self.capacity:
            self.size -= 1
            tail_key = self.__remove_tail()
            del self.cache[tail_key]

        if key not in self.cache:
            self.size += 1
        else:
            old_node = self.cache[key]
            self.__remove_node_links(old_node)
            del self.cache[key]

        node = DoublyLinkedNode(key, value)
        self.cache[key] = node
        self.__move_node_to_head(node)


if __name__ == '__main__':
    lru = LRUCache(3)
    # ["LRUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
    # [[3],       [1,1],[2,2],[3,3],[4,4],[4],   [3],  [2],  [1], [5,5], [1],  [2],  [3],  [4],  [5]]
    lru.put(1, 1)
    lru.put(2, 2)
    lru.put(3, 3)
    lru.put(4, 4)
    lru.get(4)
    lru.get(3)
    lru.get(2)
    lru.get(1)
    lru.put(5, 5)
    lru.get(1)
    lru.get(2)
    lru.get(3)
    lru.get(4)
    lru.get(5)
    ...
