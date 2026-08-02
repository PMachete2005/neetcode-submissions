class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0 
        right = left + k
        arr = []
        initmax = max(nums[left:right])
        arr.append(initmax)
        while right < len(nums):
            left += 1
            initmax = max(nums[left:right + 1])
            arr.append(initmax)
            right += 1
        return arr