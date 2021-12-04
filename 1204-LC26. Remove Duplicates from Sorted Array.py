class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # store number into a map, if number exist as key, then value return True. If value is true, remove it. If not, keep it.
        d = dict()
        i = 0
        j = 0
        ans_len = len(nums)
        while i < len(nums):
            v = nums[i]
            if v in d:
                #remove
                ans_len-=1
            else:
                d[v] = j
                j+=1
            i+=1
        for k,v in d.items():
            nums[v] = k

        return ans_len


s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums))

'''
0
[0],0,1,1,1,2,2,3,3,4
1
0,[1],1,1,2,2,3,3,4,4
2
0,1,[1],1,2,2,3,3,4,4
0,1,[1],2,2,3,3,4,4,4


'''
