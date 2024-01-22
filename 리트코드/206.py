# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail_prev = None
        while head is not None:
            tail = ListNode(head.val, tail_prev)
            tail_prev = tail
            head = head.next

        return tail_prev
