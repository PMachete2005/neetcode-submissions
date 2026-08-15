class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0], nums[1], nums[2])
        dp = [0] * len(nums)
        dp1 = [0] * len(nums)
        dp1[-1] = nums[-1]
        dp1[-2] = nums[-2]
        dp1[-3] = nums[-3]
        dp1[-4] = nums[-4] + nums[-2]
        j = len(nums) - 5
        while j >= 0:
            dp1[j] = nums[j] + max(dp1[j + 2], dp1[j + 3])
            j -= 1
        dp[-1] = nums[-1]
        dp[-2] = nums[-2]
        dp[-3] = nums[-3] + nums[-1]
        i = len(nums) - 4
        while i > 0:
            dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])
            i -= 1
        return max(dp1[0], dp[1], dp[2])
        