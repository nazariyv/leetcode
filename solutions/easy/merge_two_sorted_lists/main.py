#!/usr/bin/env python
from solutions.minions import Style, verbose, ListNode
import logging

log = logging.getLogger("merge_two_sorted_lists")

# to solve without converting to a stirng check if the reverted second half matches the first half
# starts from outwards and goes inwards
@verbose
def main(l1: ListNode, l2: ListNode) -> ListNode:
    l = ListNode()
    lnext = l
    prev = None

    while (l1 is not None and l2 is not None):
        if l1.val < l2.val: lnext.val = l1.val; l1 = l1.next
        else:               lnext.val = l2.val; l2 = l2.next
        lnext.next = ListNode()
        prev = lnext
        lnext      = lnext.next

    while l1 is not None:
        lnext.val = l1.val
        lnext.next = ListNode()
        prev = lnext
        lnext = lnext.next
        l1 = l1.next
    while l2 is not None:
        lnext.val = l2.val
        lnext.next = ListNode()
        prev = lnext
        lnext = lnext.next
        l2 = l2.next

    if prev is not None and prev.next is not None: prev.next = None

    return l


if __name__ == '__main__':
    test_cases = {
        (ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))): ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
    }
    for test, expected in test_cases.items():
        actual = main(*test)
        styler = Style.GREEN if actual == expected else Style.RED
        log.info(styler(f"actual:{actual},expected:{expected},test:{test}"))
