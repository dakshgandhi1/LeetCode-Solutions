class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dis = []
        a = {}
        heapq.heapify(dis)
        for [i,j] in points:
            d = math.sqrt(i*i + j*j)
            if d in a:
                a[d].append([i,j])
            else:
                a[d] = [[i,j]]
            heapq.heappush(dis, d)

        print(dis)
        print(a)
        res=[]
        i = 0
        while i < k:
            for j in a[heapq.heappop(dis)]:
                res.append(j)
                i+=1
        return res