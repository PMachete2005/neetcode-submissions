class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        dp = [1] * len(nums)
        maximum = -float('inf')
        for i in range(len(nums) - 2, -1, -1):
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
            if dp[i] > maximum:
                maximum = dp[i]
        return maximum
            