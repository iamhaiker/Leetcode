class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #m1: use dict to store key: num and val: count of the list nums, find key with max val
        d = dict()
        l = len(nums)
        max_count = 0
        max_key = 0
        for i in range(l):
            k = nums[i]
            if k not in d:
                d[k] = 1
            else:
                d[k]+=1
                if d[k] > max_count:
                    max_count = d[k]
                    max_key = k
        return max_key




s = Solution()
# nums = [2,2,1,1,1,2,2]
nums = [3,2,3]
print(s.majorityElement(nums))