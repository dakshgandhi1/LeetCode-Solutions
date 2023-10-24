# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [] 
        ans = 0
        res = []
        queue.append(root)
        queue.append(None)
        while len(queue) > 0:
            if queue[0] == None:
                res.append(ans)
                ans = 0
                queue.pop(0)
                if len(queue)>0:
                    queue.append(None)
                continue
            ans+=queue[0].val
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            queue.pop(0)
        
        return res.index(max(res))+1