class Solution(object):
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        '''
        m1: brute force
        max (min (x1, x2) * (id2-id1))
        
        '''

        len_h = len(height)
        max_area = 0
        for i in range(len_h):

            for j in range(i,len_h):
                left = height[i]
                right = height[j]
                min_height = min(left,right)
                area = min_height * (j-i)
                if area > max_area:
                    max_area = area
        return max_area

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        https://leetcode.com/problems/container-with-most-water/discuss/6099/Yet-another-way-to-see-what-happens-in-the-O(n)-algorithm
        """
        MAX = 0
        x = len(height) - 1
        y = 0
        while x != y:
            if height[x] > height[y]:
                area = height[y] * (x - y)
                y += 1
            else:
                area = height[x] * (x - y)
                x -= 1
            MAX = max(MAX, area)
        return MAX

s = Solution()
height = [1,8,6,2,5,4,8,3,7]
# height = [1,2,1]
print(s.maxArea(height))