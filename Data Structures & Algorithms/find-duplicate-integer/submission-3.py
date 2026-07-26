class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return nums[0]
        slow = 0 
        fast = 0
        while slow != fast or slow == 0:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        slow2 = 0 
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        return slow
        
