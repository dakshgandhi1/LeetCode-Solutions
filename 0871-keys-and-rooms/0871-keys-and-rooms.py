class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [0]*len(rooms)


        def dfs(node):
            if visited[node] == 1:
                return
            visited[node] = 1
            for i in rooms[node]:
                dfs(i)

        dfs(0)

        if 0 in visited:
            return False
        return True