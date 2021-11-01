# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pre_list = []
        post_list =[]
        lr_list = []
        rl_list= []
        self.pre_order(root,pre_list)
        self.post_order(root, post_list)
        self.lr_order(root, lr_list)
        self.rl_order(root,rl_list)

        print("pre list: {}".format(pre_list))
        print("post list: {}".format(post_list))
        print("lr list: {}".format(lr_list))
        print("rl list: {}".format(rl_list))

        return (pre_list==post_list and lr_list == rl_list)

    def pre_order(self, root, pre_list):

        if root is None:
            pre_list.append(None)
            # return None
        else:
            self.pre_order(root.left, pre_list)
            pre_list.append(root.val)
            self.pre_order(root.right, pre_list)

    def post_order(self, root, post_list):

        if root is None:
            post_list.append(None)
            # return None
        else:
            self.post_order(root.right, post_list)
            post_list.append(root.val)
            self.post_order(root.left, post_list)

    def lr_order(self, root, lr_list):

        if root is None:
            lr_list.append(None)
            # return None
        else:
            lr_list.append(root.val)
            self.lr_order(root.left, lr_list)
            self.lr_order(root.right, lr_list)


    def rl_order(self, root, rl_order):

        if root is None:
            rl_order.append(None)
            # return None
        else:
            rl_order.append(root.val)
            self.rl_order(root.right, rl_order)
            self.rl_order(root.left, rl_order)


s = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(2)
t.left.left = TreeNode(2)
t.right.left = TreeNode(2)
print(s.isSymmetric(t))