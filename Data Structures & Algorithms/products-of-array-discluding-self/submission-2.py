class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        cumproduct = 1
        cumproreverse = 1
        i = 0
        j = 0
        while i < len(nums):
            while j != i:
                cumproduct *= nums[j]
                cumproreverse *= nums[len(nums) - j - 1]
                j += 1
            prefix[i] = cumproduct
            postfix[len(nums) - 1 - i] = cumproreverse
            i += 1
        output = [0] * len(nums)
        k = 0 
        while k < len(nums):
            output[k] = prefix[k] * postfix[k]
            k += 1
        return output

            

                 

            