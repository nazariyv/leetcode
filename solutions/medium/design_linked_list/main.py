#!/usr/bin/env python
from typing import Optional


class ListNode:
    def __init__(self, val: Optional[int] = None):
        self.val: Optional[int] = val
        self.next: Optional[ListNode] = None
        self.prev: Optional[ListNode] = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: return -1

        curr: Optional[ListNode] = self.head

        for _ in range(index + 1):
            if curr is not None:
                curr = curr.next

        return -1 if curr is None else curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: return
        if index < 0:         index = 0

        self.size += 1
        pred: Optional[ListNode] = self.head

        for _ in range(index):
            if pred is not None:
                pred = pred.next

        to_add = ListNode(val)
        if pred is not None:
            to_add.next = pred.next
            pred.next = to_add
        else:
            raise Exception('never')

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        self.size -= 1
        pred: Optional[ListNode] = self.head

        for _ in range(index):
            if pred is not None:
                pred = pred.next

        if pred is not None and pred.next is not None:
            pred.next = pred.next.next
        else:
            raise Exception('never')

    def __repr__(self) -> str:
        stack = []
        n = self.head.next

        while n is not None:
            stack.append(str(n.val))
            n = n.next

        return "->".join(stack)

class DoublyLinkedList:
    def __init__(self) -> None:
        self.size = 0
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def loop_to(self, index: int, fr: ListNode, direction: str) -> ListNode:
        if direction == 'f':
            for i in range(index): fr = fr.next
        else:
            for i in range(index): fr = fr.prev
        return fr
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: return
        to_add: ListNode = ListNode(val)
        # goal is to move to pred. we can go there from head or from the tail
        # two cases. we can have odd sized or even sized linked list
        # odd:   0 1 2.  size = 3. mid is 1. move from front to 1 (exclusive). mid = size // 2 = 3 // 2 = 1
        # even: 0 1 2 3. size = 4. mid is 1. move from front to 1 (exclusive). mid = size // 2 = 4 // 2 = 2
        # when size is zero, mid is zero, when size is 1, mid is zero
        mid = self.size // 2
        pred: ListNode = None
        if index < mid: pred = self.head; pred = self.loop_to(index, pred, 'f')
        else:           pred = self.tail; pred = self.loop_to(self.size - index + 1, pred, 'b')
        succ = pred.next
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
        self.size += 1
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: return -1
        curr = self.head
        mid = self.size // 2
        if index < mid: curr = self.head; curr = self.loop_to(index + 1, curr, 'f')
        else:           curr = self.tail; curr = self.loop_to(self.size - index, curr, 'b')
        return curr.val
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return
        curr = self.head
        mid = self.size // 2
        if index < mid: curr = self.head; curr = self.loop_to(index + 1, curr, 'f')
        else:           curr = self.tail; curr = self.loop_to(self.size - index, curr, 'b')
        pred = curr.prev
        succ = curr.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
    def __repr__(self) -> str:
        stack = []
        n = self.head.next
        while n is not None and n.val is not None:
            stack.append(str(n.val))
            n = n.next
        return "->".join(stack)



if __name__ == '__main__':
    # ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
    # [[],[1],[3],[1,2],[1],[1],[1]]
    # ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
    # [[],                [7],        [2],        [1],       [3,0],        [2],           [6],       [4],       [4],    [4],        [5,0],        [6]]
    # ll = SinglyLinkedList()
    # ll.addAtHead(7)
    # ll.get(1)
    # ll.addAtHead(2)
    # ll.addAtHead(1)
    # ll.addAtIndex(3, 0)
    # ll.deleteAtIndex(2)
    # ll.addAtHead(6)
    # ll.addAtTail(4)
    # ll.get(4)
    # ll.addAtHead(4)
    # ll.addAtIndex(5, 0)
    # ll.addAtHead(6)

    # sl = SinglyLinkedList()
    # sl.addAtHead(1)
    # sl.deleteAtIndex(0)

    dll = DoublyLinkedList()
    # dll.add_at_tail(1)
    # dll.get(0)
    # dll.add_at_tail(2)
    # dll.get(0)
    # dll.add_at_head(3)
    # dll.get(0)
    # dll.add_at_tail(0)
    # dll.get(3)
    # dll.delete(1)
    # dll.delete(1)
    # dll.delete(0)
    # dll.delete(0)
    # ...
    # dll.add_at_head(7)
    # dll.add_at_tail(3)
    # dll.add_at_head(2)
    # dll.add_at_head(5)
    # dll.add_at_head(1)
    # dll.get(3)
    # ...

    # ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
    # [[],[1],[3],[1,2],[1],[1],[1]]
    dll.add_at_head(1)
    dll.add_at_tail(3)
    dll.insert_at_index(1, 2)
    dll.get(1)
    dll.delete(1)
    dll.get(1)
    ...