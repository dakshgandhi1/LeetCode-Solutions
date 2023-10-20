# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def getLeaf(self,root):
        if root.left is None and root.right is None:
            return [root.val]
        if root.left is not None and root.right is not None:
            return self.getLeaf(root.left) + self.getLeaf(root.right)
        if root.left is not None:
            return self.getLeaf(root.left)
        if root.right is not None:
            return self.getLeaf(root.right)




    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.getLeaf(root1) == self.getLeaf(root2) 
        