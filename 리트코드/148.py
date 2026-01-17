# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        ex_p1, p1, p2 = None, head, head

        while p2 and p2.next:
            ex_p1, p1, p2 = p1, p1.next, p2.next.next
        ex_p1.next = None

        lp1 = self.sortList(head)
        lp2 = self.sortList(p1)

        new_head = p = ListNode()

        while lp1 is not None and lp2 is not None:
            if lp1.val < lp2.val:
                p.next = lp1
                lp1 = lp1.next
            else:
                p.next = lp2
                lp2 = lp2.next
            p = p.next

        if lp1 is None:
            p.next = lp2
        else:
            p.next = lp1

        return new_head.next
