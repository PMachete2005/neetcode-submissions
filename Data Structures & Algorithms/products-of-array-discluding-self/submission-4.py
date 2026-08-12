class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        front = 1
        reverse = 1
        for i in range(len(nums)):
            prefix[i] = front
            postfix[- 1 - i] = reverse
            front *= nums[i]
            reverse *= nums[-1 - i]
        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * postfix[i])
        return output