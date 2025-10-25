class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        total_cost = [0 for _ in cost]

        total_cost[-1] = cost[-1]
        total_cost[-2] = cost[-2]

        for i in range(len(cost)-3, -1, -1):
            total_cost[i] = min(total_cost[i+1], total_cost[i+2]) + cost[i]
        
        return min(total_cost[0], total_cost[1])