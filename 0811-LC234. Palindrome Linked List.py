# Definition for singly-linked list.
import math
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        get len, left_len, right_len
        if odd
            left_len list in the stack
            skip middle list
            pop the stack and compare it with right_len list
        
        if even
            left_len list in the stack
             pop the stack and compare it with right_len list
        '''
        l_len = 0
        h = head
        while h is not None:
            l_len+=1
            h = h.next
        left_len = int(l_len / 2)
        right_len = left_len
        s = []
        hs = head
        if l_len%2 == 1:
            mid = (l_len+1)
            for i in range(l_len):
                if i < left_len:
                    s.append(hs)
                elif i == (mid-1):
                    pass
                else:
                    l_node = s.pop()
                    if l_node.val != hs.val:
                        return False
                hs = hs.next
        else:
            for i in range(l_len):
                if i < left_len:
                    s.append(hs)
                else:
                    l_node = s.pop()
                    print(hs.val)
                    if l_node.val != hs.val:
                        return False
                hs = hs.next
        return True



l = ListNode(1)
# l.next = ListNode(2)
# l.next.next = ListNode(2)
# l.next.next.next = ListNode(3)
# l.next.next.next.next = ListNode(1)
s = Solution()
print(s.isPalindrome(l))
