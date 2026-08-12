class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        j = goal - 1
        while j >= 0:
            if nums[j] >= (goal - j):
                goal = j
                print(goal)
            j -= 1
        if goal == 0:
            return True 
        else:
            return False
