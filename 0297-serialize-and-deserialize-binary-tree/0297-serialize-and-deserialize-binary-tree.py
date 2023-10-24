# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        l = []
        def dfs(root):
            if not root:
                l.append("#")
                return None
            l.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(l)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        nodes = data.split(",")
        self.i = 0

        def dfs():
            if nodes[self.i] == '#':
                self.i += 1
                return None
            root = TreeNode(int(nodes[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))