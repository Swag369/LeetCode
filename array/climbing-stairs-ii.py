class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        
        def cost(j, i):
            return costs[j] + (j-i)**2
        
        # cost -> i + 1 AND min remaining cost
        # cost -> i + 2 AND min remaining cost
        # cost -> i + 3 AND min remaining cost

        # min remaining cost is defined at n, n-1, n-2

        costs.insert(0,0)

        dp = [1 for _ in costs]

        dp[n] = 0
        if n >= 1:
            dp[n-1] = cost(n, n-1)
        if n >= 2:
            dp[n-2] = min(cost(n, n-2), dp[n-1] + cost(n-1, n-2))
        if n >= 3:
            dp[n-3] = min(cost(n, n-3), dp[n-1] + cost(n-1, n-3), dp[n-2] + cost(n-2, n-3))

        for i in range(n-4, -1, -1):
            dp[i] = min(dp[i+3] + cost(i+3, i), dp[i+2] + cost(i+2, i), dp[i+1] + cost(i+1, i))
        
        # print(costs)
        # print(dp)
        return dp[0]