class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        d = dict
        if d.values > 1:
            return False
        else
            return True
        '''
        d = dict()
        for n in nums:
            if n in d:
                d[n] = True
            else:
                d[n] = False
        if True in d.values():
            return True
        else:
            return False



s = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
print(s.containsDuplicate(nums))