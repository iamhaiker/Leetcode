class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums)
        sum = 0
        max_sum = -1000000
        for i in range(num_len):
            for j in range(i, num_len):
                print("i,j {}, {}".format(i,j))
                sum+=nums[j]
                if sum > max_sum:
                    max_sum = sum
                else:
                    
                # for k in range(i,j+1):
                #     sum+=nums[k]
                # if sum > max_sum:
                #     max_sum = sum
                #     sum = 0
                #     print("MAX i,j,k {}, {}, {}, sum: {}".format(i, j, nums[k], max_sum))
                # else:
                #     sum = 0
        return max_sum

s = Solution()
# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-1]
print(s.maxSubArray(nums))
