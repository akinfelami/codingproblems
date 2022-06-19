"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing 
together the nodes of the first two lists.

Return the head of the merged linked list.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        foo = []
        i = 0
        while (list1 != None):
            foo.append(list1.val)
            list1 = list1.next

            i += 1

        bar = []
        i = 0
        while (list2 != None):
            bar.append(list2.val)
            list2 = list2.next
            i += 1

        result = foo + bar
        result.sort()

        pos = 1

        if len(result) == 0:
            return None

        res = head = ListNode(result[0])

        print(len(result))
        while (pos < len(result)):
            res.next = ListNode(result[pos])
            print(pos)
            res = res.next
            pos += 1

        return head
