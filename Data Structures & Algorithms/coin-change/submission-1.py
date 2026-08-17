class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        if amount == 0:
            return 0
        for i in range(1, amount + 1):
            mincoins = float('inf')
            for c in coins:
                if c < i:
                    mincoins = min(mincoins, 1 + dp[i - c])
                    dp[i] = mincoins
                if c == i:
                    dp[i] = 1
                    break
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]

        