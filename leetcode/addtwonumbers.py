"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res1 = ''
        res2 = ''

        while (l1 != None or l2 != None):
            if(l1 != None):
                res1 = str(l1.val)+res1
                l1 = l1.next

            if(l2 != None):
                res2 = str(l2.val)+res2
                l2 = l2.next

        foo = int(res1)
        bar = int(res2)

        sum = foo + bar

        s = str(sum)

        last = len(s) - 1

        a = int(s[last])

        result = ListNode(a)
        p = result

        for i in range(last-1, -1, -1):
            x = ListNode(int(s[i]))
            p.next = x
            p = p.next

        return result
