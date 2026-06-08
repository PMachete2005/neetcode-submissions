class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        arr = []
        for i in range(len(nums)):
            toCheck = target - nums[i]
            if toCheck in myMap:
                arr.append(myMap[toCheck])
                arr.append(i)
                return arr
            else:
                myMap[nums[i]] = i
                continue
        return arr
        

        


                
        