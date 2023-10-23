# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [] 
        ans = []
        res = []
        queue.append(root)
        queue.append(None)
        while len(queue) > 0:
            if queue[0] == None:
                if len(ans)>0:
                    res.append(ans)
                    ans = []
                    queue.append(None)
                queue.pop(0)
                continue
            ans.append(queue[0].val)
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            queue.pop(0)
        
        return res
            

