class Solution:
    def addTwoNumbers(self, l1, l2):
        d1 = collections.deque()
        d2 = collections.deque()

        if l1 == None:
            return l2

        if l2 == None:
            return l1

        while l1 != None:
            d1.appendleft(str(l1.val))
            l1 = l1.next

        while l2 != None:
            d2.appendleft(str(l2.val))
            l2 = l2.next

        str1 = "".join(d1)
        str2 = "".join(d2)

        res = (str(eval(str1+"+"+str2)))
        l3 = ListNode()
        l3_p = l3

        for i in range(len(res)-1, 0, -1):
            l3_p.val = int(res[i])
            if i != 0 :
                l3_p.next = ListNode()
                l3_p = l3_p.next
        l3_p.val = int(res[0])
        return l3