# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(root, p, q):
            if not root:
                return None
            if root == p or root == q:
                return root
            a = dfs(root.left, p, q)
            b = dfs(root.right, p, q)
            if a and b:
                return root
            elif a:
                return a
            else:
                return b

        return dfs(root, p, q)