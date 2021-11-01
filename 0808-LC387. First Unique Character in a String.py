'''
Min Deletions to Make Frequency of Each Letter Unique
Min Swaps to Make Palindrome
Min Steps to Make Piles Equal Height
Largest K such that both K and -K exist in array
Max Length of a Concatenated String with Unique Characters
Unique Integers That Sum Up To 0
Partition array into N subsets with balanced sum
Jump Game [Experienced]
Meeting Rooms II
Count Visible Nodes in Binary Tree
Largest Alphabetic Character

https://leetcode.com/discuss/interview-question/398023/Microsoft-Online-Assessment-Questions
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        # m1
        '''
        dict: key is string, value is count
        find first counts == 1
        '''

        d = {}
        for i in range(len(s)):
            w = s[i]
            if w in d:
                d[w]+=1
            else:
                d[w]=0

        for j in range(len(s)):
            w = s[j]
            if d[w] == 0:
                return j
            elif j == (len(s)-1):
                return -1


s = Solution()
t = "loveleetcode"
print(s.firstUniqChar(t))