class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next

            head.next = self.swapPairs(p.next)

            p.next = head
            return p
        return head