class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        mySet = set()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tempsum = sortedNums[i] + sortedNums[j] + sortedNums[k]
                if  tempsum > 0:
                    k -= 1
                elif tempsum < 0:
                    j += 1
                else:
                    oplist = [sortedNums[i], sortedNums[j], sortedNums[k]]
                    mySet.add(tuple(oplist))
                    j += 1
                    k -= 1
        return list(mySet)


            

            





        

            


