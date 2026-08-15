class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0] * len(nums)
        dp[-1] = nums[-1]
        dp[-2] = nums[-2]
        dp[-3] = nums[-3] + nums[-1]
        i = len(nums) - 4
        while i >= 0:
            dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])
            i -= 1
        return max(dp[0],dp[1])