# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        if p is None:
            return p

        next_p = p.next
        new_head = None
        ex_p = None

        while p is not None and next_p is not None:
            new_p_next = next_p.next

            if ex_p is None:
                new_head = next_p
            else:
                ex_p.next = next_p

            p.next = new_p_next
            next_p.next = p

            ex_p = p
            p = p.next
            if p is None:
                break
            next_p = p.next

        return new_head if new_head is not None else head
