class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #m1: Sort
        '''
        l = len(nums)
        # bubble sort
        for i in range(l):
            n = nums[i]
            if n == 0:
                nums[i] = (2**31 - 1)

        for i in range(l):
            already_sorted = True

            for j in range(l-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                already_sorted = False

            if already_sorted:
                break

        for i in range(l):
            n = nums[i]
            if n == (2**31 - 1):
                nums[i] = 0
        return nums
        '''
        l = len(nums)
        for i in range(l):
            already_sorted = True

            for j in range(l-i-1):
                if nums[j] == 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                already_sorted = False
            if already_sorted:
                break
        return nums


# m2:
'''
public void moveZeroes(int[] nums) {
    if (nums == null || nums.length == 0) return;        

    int insertPos = 0;
    for (int num: nums) {
        if (num != 0) nums[insertPos++] = num;
    }        

    while (insertPos < nums.length) {
        nums[insertPos++] = 0;
    }
}
'''


s = Solution()
nums = [0,1,0,3,12]
print(s.moveZeroes(nums))
