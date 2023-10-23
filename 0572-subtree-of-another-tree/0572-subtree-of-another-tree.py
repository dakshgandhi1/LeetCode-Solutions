# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def isIdentical(self, root, subroot):
        if not root and not subroot:
            return True
        if not root or not subroot:
            return False
        if root.val == subroot.val:
            return self.isIdentical(root.left, subroot.left) and self.isIdentical(root.right, subroot.right)
        return False

    def isSubtree(self, root, subroot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not subroot:
            return True
        if not root:
            return False
        if root.val == subroot.val:
            if self.isIdentical(root, subroot):
                return True

        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot) 