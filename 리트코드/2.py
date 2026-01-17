# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str = ""
        l2_str = ""
        tail_prev = None

        while l1 is not None:
            l1_str += str(l1.val)
            l1 = l1.next

        while l2 is not None:
            l2_str += str(l2.val)
            l2 = l2.next

        new_str = str(int(l1_str[::-1]) + int(l2_str[::-1]))

        for v in new_str:
            tail = ListNode(v, tail_prev)
            tail_prev = tail

        return tail_prev
