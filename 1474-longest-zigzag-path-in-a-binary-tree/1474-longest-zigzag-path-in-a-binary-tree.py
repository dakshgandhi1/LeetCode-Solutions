# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, isLeft, depth):
            if not root:
                return depth
            if isLeft:
                depth = max(depth, dfs(root.left, False, depth+1) , dfs(root.right, True, 0))
            else:
                depth = max(depth, dfs(root.right, True, depth+1) , dfs(root.left, False, 0))

            return depth

        return max(dfs(root.left, False, 0), dfs(root.right, True, 0))