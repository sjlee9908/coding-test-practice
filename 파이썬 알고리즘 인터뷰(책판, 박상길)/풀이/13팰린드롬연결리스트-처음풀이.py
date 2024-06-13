# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def isPalindrome(self, head: [ListNode]) -> bool:
        res = []
        p = head
        while p != None:
            res.append(p.val)
            p = p.next

        return res == res[::-1]


