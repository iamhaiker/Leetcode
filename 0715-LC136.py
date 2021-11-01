class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums)
        d = {}
        for i in range(num_len):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        return min(d)
        # for j in range(num_len):
        #     if d[nums[j]] == 1:
        #         return nums[j]

s = Solution()
nums = [4,1,2,1,2]
print(s.singleNumber(nums))