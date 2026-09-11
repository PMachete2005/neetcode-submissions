class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cursum = 0
        maxsum = -float('inf')
        i = 0 
        while i < len(nums):
            cursum += nums[i]
            maxsum = max(cursum, maxsum)
            if cursum < 0:
                cursum = 0
            i += 1
        return maxsum
        



        