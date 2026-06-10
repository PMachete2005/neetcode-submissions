class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        opList = [0] * len(nums)
        product = 1
        reverseproduct = 1
        i = 0
        while i < len(nums):
            product = product * nums[i]
            prefix[i] = product
            reverseproduct = reverseproduct * nums[-1 - i]
            postfix[-1 - i] = reverseproduct
            i = i + 1
        i = 0
        while i < len(nums):
            if i == 0:
                opList[0] = postfix[1]
            elif i == (len(nums) - 1):
                opList[i] = prefix[i - 1]
            else:
                opList[i] = (postfix[i + 1]) * (prefix[i - 1])
            i = i + 1
        return opList