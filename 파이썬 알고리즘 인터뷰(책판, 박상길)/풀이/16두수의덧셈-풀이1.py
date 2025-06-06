import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        def reverseList(self, head):
            node, prev = head, None
            while node:
                next, node.next = node.next, prev
                prev, node = node, next
            return prev

        def toList(self, node):
            list = []
            while node:
                list.append(node.val)
                node = node.next
            return list

        def toReverseLinkedList(self, result):
            prev = None
            for r in result:
                node = ListNode(r)
                node.next = prev
                prev = node
            return node

        def addTwoNumbers(self, l1, l2):
            a = self.toList(self.reverseList(l1))
            b = self.toList(self.reverseList(l2))

            resultStr = int(''.join(str(e) for e in a) + int(''.join(str(e) for e in b)))
            return self.toReverseLinkedList(str(resultStr))

