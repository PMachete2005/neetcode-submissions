class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0 
        jumps = 0
        while i != len(nums) - 1:
            maxindex = i + nums[i]
            if maxindex >= len(nums) - 1:
                jumps += 1
                break
            j = maxindex
            while j != i:
                if (j - i) + nums[j] > ((maxindex - i) + nums[maxindex]):
                    maxindex = j 
                j -= 1
            i = maxindex
            jumps += 1
        return jumps
        