class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        tmp = ""
        self.genParenthesisUtil(n, n, tmp, result)
        return result

    def genParenthesisUtil(self, left, right, tmp, result):

        if left == 0 and right == 0:
            result.append(tmp)
            return

        if left > 0:
            self.genParenthesisUtil(left - 1, right, tmp + "(", result)
        if right > left:
            self.genParenthesisUtil(left, right - 1, tmp + ")", result)


s = Solution()
n = 3
print(s.generateParenthesis(n))
