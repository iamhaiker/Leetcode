# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = None
        i=0
        n = len(nums)
        ans = self.insertLevel(root, nums, i,n)
        return ans

    def insertLevel(self,root, nums, i, n):
        if i < n:
            tmp = TreeNode(nums[i])
            root = tmp
            root.left = self.insertLevel(root.left,nums, 2*i+1,n)
            root.right = self.insertLevel(root.right,nums, 2*i+2,n)
        return root

    def printInOrder(self,root):
        if root is None:
            return None
        else:
            self.printInOrder(root.left)
            print(root.val)
            self.printInOrder(root.right)

s = Solution()
nums = [1,2,3,4,5]
r = s.sortedArrayToBST(nums)
s.printInOrder(r)