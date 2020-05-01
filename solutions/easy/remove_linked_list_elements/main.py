#!/usr/bin/env python
from solutions.minions import ListNode


def remove_elements(head: ListNode, val: int) -> ListNode:
    while head is not None and head.val == val:
        head = head.next if head.next else None

    prev = head
    curr = head.next if head is not None else None

    while curr is not None:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next

    return head


if __name__ == '__main__':
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(3)))))
    print(remove_elements(l, 3))
