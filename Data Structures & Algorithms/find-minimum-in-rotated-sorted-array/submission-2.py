class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if (mid == 0 and nums[1] > nums[0]) or nums[mid - 1] > nums[mid]:
                return nums[mid]
            else:
                if nums[right] < nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        