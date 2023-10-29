class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        edges = {(a,b) for a,b in connections}
        print(edges)
        neighbours = {city:[] for city in range(n)}
        print(neighbours)
        visit = set()
        changes = 0

        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)
        print(neighbours)

        def dfs(city):
            nonlocal edges, neighbours, visit, changes

            for nei in neighbours[city]:
                if nei in visit:
                    continue
                if (nei, city) not in edges:
                    changes+=1
                visit.add(nei)
                dfs(nei)

        visit.add(0)
        dfs(0)
        return changes