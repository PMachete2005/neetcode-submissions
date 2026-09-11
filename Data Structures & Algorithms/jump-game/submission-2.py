class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = len(nums) - 1 
        while index != 0:
            j = index - 1
            while j != 0:
                if nums[j] >= (index - j):
                    index = j 
                    break
                j -= 1
            if nums[j] >= (index - j):
                index = j
            else:
                return False
        return True
            
        
        