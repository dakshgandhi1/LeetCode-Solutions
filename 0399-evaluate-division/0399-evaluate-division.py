class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

        dic = collections.defaultdict(dict)

        for  (x,y), value in zip(equations, values):
            dic[x][y] = value
            dic[y][x] = 1/value

        print(dic)
        def dfs(x, y, visit):
            if x not in dic and y not in dic:
                return -1
            if y in dic[x]: return dic[x][y]

            for i in dic[x]:
                if i in visit: continue
                visit.add(i)
                temp = dfs(i, y, visit)
                if temp == -1: continue
                else: return dic[x][i] * temp

            return -1

        res = []
        for x, y in queries:
            res.append(dfs(x,y,set()))

        return res