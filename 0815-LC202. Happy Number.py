class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # m1
        '''
        sum = n
        # use a dict to record whether current sum has been calculated before, if yes, then it's a cycle, return False
        d = {}
        # d[n] = True
        if sum == 1:
            return True

        while sum != 1:
            if sum in d:
                return False
            d[sum] = True
            sum = self.square_digits(sum)
            if sum == 1:
                return True
        return False
        '''
        #m2
        slow = fast = n
        while slow!=fast:
            slow = self.square_digits(slow)
            fast = self.square_digits(fast)
            fast = self.square_digits(fast)
        if slow ==1:
            return True
        else:
            return False


    def square_digits(self, n):
        sn = str(n)
        square_sum = 0
        # calculate square of digits
        for i in range(len(sn)):
            d = int(sn[i])
            square_sum += d**2
        return square_sum

s= Solution()
n = 2
print(f'this is {s.isHappy(n)}')