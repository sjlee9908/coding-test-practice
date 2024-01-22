    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        now_idx = 0
        p = head
        reverse_ll_p = None
        reverse_ll_tail = None
        left_left = None
        right_right = None

        while p is not None:
            now_idx += 1
            if now_idx + 1 == left:
                left_left = p

            if now_idx-1 == right:
                right_right = p

            if left <= now_idx <= right:
                reverse_ll_p = ListNode(p.val, reverse_ll_p)
                if reverse_ll_tail is None:
                    reverse_ll_tail = reverse_ll_p

            p = p.next

        if reverse_ll_tail is not None:
            reverse_ll_tail.next = right_right

        if left_left is None:
            return reverse_ll_p
        else:
            left_left.next = reverse_ll_p
            return head
