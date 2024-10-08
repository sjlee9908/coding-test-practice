# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        origin_head = head = ListNode()

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            head.next = ListNode(list1.val, None)
            head = head.next
            list1 = list1.next
        else:
            head.next = ListNode(list2.val, None)
            head = head.next
            list2 = list2.next

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                head.next = ListNode(list1.val, None)
                head = head.next
                list1 = list1.next
            else:
                head.next = ListNode(list2.val, None)
                head = head.next
                list2 = list2.next

        if list1 is not None:
            head.next = list1

        if list2 is not None:
            head.next = list2

        return origin_head.next

