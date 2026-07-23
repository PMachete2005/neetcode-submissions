class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        output = []
        i = 0 
        while i < len(nums):
            toCheck = target - nums[i]
            if toCheck in myMap:
                output.append(myMap[toCheck])
                output.append(i)
                return output
            else:
                myMap[nums[i]] = i
                i += 1 
        
        
        


                
        