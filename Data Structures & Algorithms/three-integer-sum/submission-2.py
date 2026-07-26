class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #We will have to sort the array first
        mySet = set()
        sortedNums = sorted(nums)
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if sortedNums[j] + sortedNums[k] + sortedNums[i] > 0:
                    k -= 1
                elif sortedNums[j] + sortedNums[k] + sortedNums[i] < 0:
                    j += 1
                else:
                    mySet.add(tuple([sortedNums[j],sortedNums[k],sortedNums[i]]))
                    k -= 1
                    j += 1
        return list(mySet)
            

            

            





        

            


