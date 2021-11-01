class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1_len = m
        for i in range(nums1_len):
            nums1[m+n-i-1] = nums1[nums1_len-i-1]
        print(nums1)
        total_len = (m + n)
        j = total_len-m
        k = 0
        l = 0
        while l < total_len:
            # print("j,k,l: {}, {}, {}".format(j,k,l))
            if j>=total_len and k >=n:
                return nums1
            elif j>=total_len:
                nums1[l] = nums2[k]
                k+=1
            elif k>=n:
                nums1[l] = nums1[j]
                j += 1
            elif nums1[j] < nums2[k]:
                nums1[l] = nums1[j]
                j+=1
            else:
                nums1[l] = nums2[k]
                k+=1
            l+=1
        # print(nums1)
        return nums1


s = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m= 3
n = 3
# nums1 = [0]
# m=0
# nums2 = [1]
# n =1
print(s.merge(nums1,m,nums2,n))


"""
[1,2,3,0,0,0]

[1,2,3,1,2,3]
[2,5,6]

[1,2,2,3,5,6]

6-3=3

"""