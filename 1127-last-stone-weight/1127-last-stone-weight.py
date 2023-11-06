class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -abs(x-y))

        if len(stones) == 0:
            return 0
        return -stones[0]