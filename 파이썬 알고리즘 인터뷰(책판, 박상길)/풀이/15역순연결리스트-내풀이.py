# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        dq = collections.deque()

        while head != None:
            dq.appendleft(head.val)
            head = head.next

        res = ListNode()
        res_p = res
        while len(dq) != 0:
            res_p.val = dq.popleft()
            if len(dq) != 0:
                res_p.next = ListNode()
            res_p = res_p.next

        return res
