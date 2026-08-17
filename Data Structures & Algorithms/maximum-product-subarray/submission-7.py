class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxproduct = nums[0]
        minproduct = nums[0]
        toreturn = nums[0]
        for i in range(1, len(nums)):
            curmin = minproduct
            curmax = maxproduct
            if nums[i] < 0:
                toreturn = max(nums[i] * minproduct, nums[i], toreturn)
                minproduct = min(nums[i] * curmax, nums[i])
                maxproduct = max(nums[i] * curmin, nums[i])
            else:
                toreturn = max(nums[i] * maxproduct, nums[i], toreturn)
                minproduct = min(nums[i] * curmin, nums[i])
                maxproduct = max(nums[i] * curmax, nums[i])
        return toreturn







        