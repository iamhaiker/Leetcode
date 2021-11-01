class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)+1
        s = set()
        for i in range(n):
            s.add(i)

        for i in range(len(nums)):
            s.remove(nums[i])
        # if len(s) == 1:
        return s.pop()

s = Solution()
# a = [3,0,1]
# a = [9,6,4,2,3,5,7,0,1]
a = [0]
print(s.missingNumber(a))



