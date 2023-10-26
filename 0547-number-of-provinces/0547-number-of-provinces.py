class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = [0]*len(isConnected)
        def dfs(node):
            if visited[node] == 1:
                return
            visited[node] = 1
            for i in range(len(isConnected[node])):
                if i == node:
                    continue
                if isConnected[node][i] == 1:
                    dfs(i)
        
        num=0
        for i in range(len(isConnected)):
            if visited[i] == 0:
                num+=1
                dfs(i)

        return num