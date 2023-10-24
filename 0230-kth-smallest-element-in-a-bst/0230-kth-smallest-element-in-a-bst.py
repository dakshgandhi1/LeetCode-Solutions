# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        inorder = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            try:
                if len(inorder) >= k:
                    raise Exception("Found")
            except:
                return
            inorder.append(root.val)
            dfs(root.right)

        dfs(root)
        return inorder[-1]