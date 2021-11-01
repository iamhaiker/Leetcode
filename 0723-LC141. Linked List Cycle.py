# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # method 1: brute force, two loops, check whether it's the same node.
        # return self.method1(head)

        # method 2: put node into set, check whether in the set
        return self.method2(head)

    def method1(self, head):

        if head is None:
            return False
        first = head

        while first is not None:
            second = first.next
            while second is not None:
                if first is second:
                    return True
                second = second.next
            if second is None:
                return False
            else:
                first = first.next

        return False

    def method2(self, head):
        s = set()
        h = head

        while h not in s:
            if h is None:
                return False
            s.add(h)
            h = h.next
        return True

s = Solution()
l = ListNode(3)
l.next = ListNode(2)
l.next.next = ListNode(2)
l.next.next.next = ListNode(-4)
l.next.next.next.next = l.next.next
print(s.hasCycle(l))