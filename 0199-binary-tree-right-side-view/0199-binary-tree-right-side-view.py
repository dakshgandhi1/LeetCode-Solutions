# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        view = {}
        def rightView(root, view, level):
            if not root:
                return
            if view.has_key(level) == False:
                view[level] = root.val
            rightView(root.right, view, level+1)
            rightView(root.left, view, level+1)

        rightView(root, view, 0)
        return view.values()