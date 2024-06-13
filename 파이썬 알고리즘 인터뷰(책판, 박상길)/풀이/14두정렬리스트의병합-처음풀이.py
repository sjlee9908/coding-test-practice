# Definition for singly-linked list.

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None and list2 != None:
            return list2
        elif list1 != None and list2 ==None:
            return list1

        nlist = ListNode()
        nlist_p = nlist

        while (list1 != None) and (list2 != None):
            if list1.val > list2.val:
                nlist_p.val = list2.val
                list2 = list2.next
            else:
                nlist_p.val = list1.val
                list1 = list1.next
            if (list1 != None) and (list2 != None):
                nlist_p.next = ListNode()
                nlist_p = nlist_p.next

        if list1 == None:
            nlist_p.next = list2

        if list2 == None:
            nlist_p.next = list1

        return nlist
