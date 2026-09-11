class Solution:
    def jump(self, nums: List[int]) -> int:
        i = len(nums) - 1 
        jumps = 0
        while i != 0:
            j = i - 1
            k = i
            while j != 0:
                if nums[j] >= (i - j):
                    k = j
                j -= 1
            if nums[j] >= (i - j):
                k = j
            i = k
            jumps += 1
        return jumps
        