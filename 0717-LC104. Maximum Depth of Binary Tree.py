# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = 0
        ans = []
        self.max_depth(root,d,ans)
        return max(ans)

    # method 1
    def max_depth(self,root,d,ans):

        if root is None:
            return None
        else:
            self.max_depth(root.left,d+1,ans)
            ans.append(d)
            self.max_depth(root.right,d+1,ans)
        return ans

    #method 2
    def maxDepth2(self,root):
        if root is None:
            return 0
        return 1+max(self.maxDepth2(root.left),self.maxDepth2(root.right))



s= Solution()
t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.right = TreeNode(7)
t.right.left = TreeNode(15)
# print(s.maxDepth(t))
print(s.maxDepth2(t))