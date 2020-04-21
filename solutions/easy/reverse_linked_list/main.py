#!/usr/bin/env python
from solutions.minions import TestCase as T, TestRunner as TR, ListNode


def main(head: ListNode) -> ListNode:
    prev_node = None
    curr_node = head
    while curr_node:
        next_node = curr_node.next # Remember next node
        curr_node.next = prev_node  # REVERSE! None, first time round.
        prev_node = curr_node  # Used in the next iteration.
        curr_node = next_node  # Move to next node.
    head = prev_node
    return head

# prev, next, actual_next
def reverse_list(head: ListNode) -> ListNode:
    if head is None: return None
    prev = head
    next = prev.next
    prev.next = None
    if next is None: return head
    actual_next = next.next
    next.next = prev
    prev = next
    while actual_next is not None:
        next_ = actual_next.next
        actual_next.next = prev
        prev = actual_next
        actual_next = next_
    return prev



if __name__ == '__main__':
    TR((
        T(ListNode(1,ListNode(2, ListNode(3))), ListNode(3, ListNode(2, ListNode(1)))),
        T(ListNode(1), ListNode(1)),
        T(ListNode(2, ListNode(5)), ListNode(5, ListNode(2)))
    ,), reverse_list)()
