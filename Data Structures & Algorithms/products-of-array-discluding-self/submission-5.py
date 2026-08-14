class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        front = 1 
        back = 1 
        for i in range(len(nums)):
            left[i] = front 
            right[len(nums) - 1 - i] = back 
            front *= nums[i]
            back *= nums[len(nums) - 1 - i]
        output = []
        for i in range(len(nums)):
            output.append(left[i] * right[i])
        return output

            

                 

            