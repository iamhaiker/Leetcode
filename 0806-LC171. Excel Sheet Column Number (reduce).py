class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        #m1
        # dict map key alphabet to value num
        d = {}

        str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, s in enumerate(str):
            # add to dict
            d[s]=i+1

        level=0
        sum = 0
        for pos in range(len(columnTitle)-1,-1,-1):
            s = columnTitle[pos]
            n = d[s]
            sum+=n*pow(26,level)
            level+=1

        # m2
        '''
        return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])
    
        '''
        return sum




s = Solution()
print(s.titleToNumber("BA"))

'''


A = 1 = 26^0
AA = 1*26^1+26^0
BA = 2*26^1+26^0=53
11 = 1*10^1 + 10^0
21 = 2*10^1 + 10^0
AAA =26*26+26+1
'''

# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))