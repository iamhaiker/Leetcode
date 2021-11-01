# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        add_num = 0
        ans = ListNode()
        rtn = ans
        t1 = l1
        t2 = l2

        while t1 is not None or t2 is not None or add_num !=0:
            if t1 is None and t2 is not None:
                n2 = t2.val
                t1 = ListNode()
                n1 = 0
            elif t2 is None and t1 is not None:
                n1 = t1.val
                t2 = ListNode()
                n2 = 0
            elif t1 is not None and t2 is not None:
                n1 = t1.val
                n2 = t2.val
            elif add_num!=0:
                ans.next = ListNode(add_num)
                break
            s = n1+n2+add_num
            add_num = 0
            if s >= 10:
                add_num = int(str(s)[0])
                cur_num = int(str(s)[1])
            else:
                cur_num = int(str(s)[0])
            ans.next = ListNode(cur_num)
            ans = ans.next
            t1 = t1.next
            t2 = t2.next
        return rtn.next

        #m1
        '''
        add_num = 0
        idx = 0
        max_len = max(len(l1),len(l2))
        ans = []
        len1 = len(l1)
        len2 = len(l2)

        while idx < max_len or add_num !=0:
            if idx < max_len:
                if idx > len1-1:
                    n2 = l2[idx]
                    n1 = 0
                elif idx > len2-1:
                    n1= l1[idx]
                    n2 = 0
                else:
                    n1 = l1[idx]
                    n2 = l2[idx]
                s = n1+n2+add_num
                add_num = 0
                if s >= 10:
                    add_num = int(str(s)[0])
                    cur_num = int(str(s)[1])
                else:
                    cur_num = int(str(s)[0])
                ans.append(cur_num)
            elif add_num!=0:
                ans.append(add_num)
                add_num = 0
            idx+=1

        return ans
        '''





s = Solution()

# l1=[9,9,9,9,9,9,9]
# l2=[9,9,9,9]
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(s.addTwoNumbers(l1,l2))
