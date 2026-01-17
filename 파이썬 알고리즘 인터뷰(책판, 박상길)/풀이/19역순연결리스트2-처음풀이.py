# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        root = ListNode()
        root.next = head

        p1 = root
        right_p = head
        node_stack = []

        for i in range(1, left):
            p1 = p1.next
        left_p = p1.next

        for i in range(1, right):
            right_p = right_p.next
        p2 = right_p.next

        new_right_p = left_p

        while left_p != right_p:
            node_stack.append(left_p)
            left_p = left_p.next

        new_left_p = right_p

        while node_stack:
            node = node_stack.pop()
            right_p.next = node
            right_p = right_p.next

        p1.next = new_left_p
        new_right_p.next = p2

        return root.next


