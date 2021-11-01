# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    ans = []
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return None
        else:
            self.inorderTraversal(root.left)
            self.ans.append(root.val)
            self.inorderTraversal(root.right)
            # print(self.ans)
        return self.ans

s = Solution()
# t = TreeNode()
t = TreeNode(1)
# t.right = TreeNode(2)
# t.right.left = TreeNode(3)
print(s.inorderTraversal(t))


# # recursively
# def inorderTraversal1(self, root):
#     res = []
#     self.helper(root, res)
#     return res
#
#
# def helper(self, root, res):
#     if root:
#         self.helper(root.left, res)
#         res.append(root.val)
#         self.helper(root.right, res)