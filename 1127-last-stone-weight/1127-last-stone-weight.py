class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * i for i in stones]
        print(stones)
        heapq.heapify(stones)
        while len(stones)>1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -1*abs(x-y))

        if len(stones) == 0:
            return 0
        return stones[0] * -1