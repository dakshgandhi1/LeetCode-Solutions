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
            if root.val == p.val or root.val == q.val:
                return root
            a = dfs(root.left, p, q)
            b = dfs(root.right, p, q)
            if a != None and b != None:
                return root
            elif a!=None:
                return a
            else:
                return b

        return dfs(root, p, q)