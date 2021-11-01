# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = []
        f = l1
        s = l2

        while f is not None or s is not None:
            if f is None:
                ans.append(s.val)
                s = s.next
            elif s is None:
                ans.append(f.val)
                f = f.next
            else:
                if f.val <= s.val:
                    ans.append(f.val)
                    f = f.next
                else:
                    ans.append(s.val)
                    s = s.next
        print(ans)

        rtn = ansLS = ListNode()
        for i in range(len(ans)):
            ansLS.next = ListNode(ans[i])
            ansLS = ansLS.next
        return rtn.next


l2 = l1 = t1= ListNode(1)
t1.next = ListNode(2)
t1 = t1.next
t1.next = ListNode(4)
t1 = t1.next

s = Solution()
s.mergeTwoLists(l1,l2)


