class Solution:
    def isPalindrome(self, head: [ListNode]) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:  #만약 입력값이 홀수일때(fast.next == None), 중앙을 비껴나기 위해서 한번더 이동
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev  #정상적으로 비교가 끝나면 rev는 None