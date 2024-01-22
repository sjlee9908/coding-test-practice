# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_p = odd_head = ListNode(-1, None)
        even_p = even_head = ListNode(-1, None)
        p = head
        i = 1

        while p is not None:
            p_next = p.next

            if i % 2 == 0:
                even_p.next = p
                even_p = even_p.next
            else:
                odd_p.next = p
                odd_p = odd_p.next

            p = p_next
            i += 1
        even_p.next = None
        odd_p.next = even_head.next
        return odd_head.next
