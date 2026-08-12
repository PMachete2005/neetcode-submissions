class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        j = 0
        curmax = 0
        res = -float('inf')
        for j in range(len(nums)):
            curmax += nums[j] 
            res = max(res, curmax)
            if curmax < 0:
                curmax = 0 
                continue
        return res
            