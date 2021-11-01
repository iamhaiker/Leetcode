# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode()
        ans = h
        stack = []

        while head is not None:
            stack.append(head.val)
            head = head.next

        while len(stack):
            s = stack.pop()
            h.next = ListNode(s)
            h = h.next

        return ans.next

    def printList(self, list):

        while list is not None:
            # print(list.val)
            list = list.next



s = Solution()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
s.printList(s. reverseList(l))

