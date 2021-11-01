class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        sLen = len(s)
        i = 0
        #  even length
        if sLen%2 == 0:
            # 0,1,2,3
            # 1,2
            # 0,3
            # half = 1
            half = int(sLen / 2) - 1
            while i <= half:
                tmp = s[half + i + 1]
                s[half + i + 1] = s[half - i]
                s[half - i] = tmp
                i += 1
        ## odd length
        else:
            half = int(sLen / 2)
            while i <= half:
                tmp = s[half + i]
                s[half + i] = s[half - i]
                s[half - i] = tmp
                i += 1
        print(s)
        return s


s = Solution()
a = ["h","e","l","l","o"]
s.reverseString(a)
