class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost[0], cost[1])
        dp = [0] * (len(cost) + 1)
        dp[-2] = cost[-1]
        i = len(cost) - 2
        while i >= 0:
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
            i -= 1
        return min(dp[0], dp[1])