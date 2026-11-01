class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # We want to always take the 2 smallest sticks to minimze cost
        # We will combine 2 sticks until only 1 is left
        total_cost = 0

        heapq.heapify(sticks)

        while len(sticks) > 1:
            smallest = heapq.heappop(sticks)
            second_smallest = heapq.heappop(sticks)
            cost = smallest + second_smallest
            total_cost += cost
            heapq.heappush(sticks, cost)
        
        return total_cost