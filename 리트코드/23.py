# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        new_head = tail = ListNode()

        while lists != [None] * len(lists):
            for i in range(len(lists)):
                if lists[i] is not None:
                    heapq.heappush(heap, lists[i].val)
                    lists[i] = lists[i].next

            tail.next = ListNode(heapq.heappop(heap))
            tail = tail.next

        while heap:
            tail.next = ListNode(heapq.heappop(heap))
            tail = tail.next


        return new_head.next