#!/usr/bin/env python
from solutions.minions import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_node  = head
        last_odd_node = odd_node

        even_head = head.next
        even_node = even_head

        while odd_node:
            # if just two nodes: 1 -> 2. Then nothing happens
            if odd_node.next:
                odd_node.next  = odd_node.next.next

            # if 1 -> 2 -> 3. Then I need to set next of 2 to None
            if even_node:
                if even_node.next:
                    even_node.next = even_node.next.next
                else:
                    even_node.next = None

            last_odd_node = odd_node
            odd_node      = odd_node.next   # type: ignore
            if even_node:
                even_node     = even_node.next  # type: ignore

        last_odd_node.next = even_head

        return head


if __name__ == '__main__':
    Solution().oddEvenList(ListNode(1, ListNode(2, ListNode(3))))
    ...
