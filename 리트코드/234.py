import collections


class Solution:
    def isPalindrome(self, head: [ListNode]) -> bool:
        node_val_list = collections.deque()

        while head is not None:
            node_val_list.append(head.val)
            head = head.next

        node_val_list = list(node_val_list)
        return node_val_list == node_val_list[::-1]
