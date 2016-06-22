# =============================================================================
#   FileName: 2.AddTwoNumbers.py
#    Example:
#       Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#       Output: 7 -> 0 -> 8
#     Author: Marslo
#      Email: marslo.jiao@gmail.com
#    Created: 2016-06-21 18:03:20
#    Version: 0.0.1
# LastChange: 2016-06-22 21:28:29
# =============================================================================


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# idx = ListNode(3)
# n = idx
# n.next = ListNode(4)
# n = n.next
# n.next = ListNode(5)
# n = n.next
# return idx
# ----> 3 -> 4 -> 5

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x = 0
        idx = None
        while l1 and l2:
            res = (x + l1.val + l2.val) % 10
            x = (x + l1.val + l2.val) / 10

            if not idx:
                idx = ListNode(res)
                n = idx
            else:
                n.next = ListNode(res)
                n = n.next

            l1 = l1.next
            l2 = l2.next

        if l1:
            l = l1
        else:
            l = l2

        while l:
            n.next = ListNode((x + l.val) % 10)
            n = n.next
            x = (x + l.val) / 10
            l = l.next

        while x != 0:
            n.next = ListNode(x % 10)
            n = n.next
            x = x / 10

        return idx


l11 = [2, 4, 3]
l12 = [5, 6, 4]
r1 = [7, 0, 8]

l21 = [15, 8, 7]
l22 = [5, 3, 3]
r2 = [0, 3, 1, 1]

s = Solution()

if r1 != s.addTwoNumbers(l11, l12):
    print s.addTwoNumbers(l11, l12)
    print '1 failed'
else:
    print '1 succeed'


if r2 != s.addTwoNumbers(l21, l22):
    print s.addTwoNumbers(l21, l22)
    print '2 failed'
else:
    print '2 succeed'
