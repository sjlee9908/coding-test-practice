# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    node_list = []
    def sortList(self, head):
        p = head

        while p is not None:
            self.node_list.append(p.val)
            p = p.next

        self.node_list.sort()

        p = head
        while p is not None:
            p.val = self.node_list.pop(0)
            p = p.next

        return head