class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        oplist = []
        mySet = set()
        numSorted = sorted(nums)
        i = 0 
        while i < (len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if numSorted[i] + numSorted[j] + numSorted[k] > 0:
                    k -= 1
                elif numSorted[i] + numSorted[j] + numSorted[k] < 0:
                    j += 1
                else:
                    mySet.add(tuple([numSorted[i], numSorted[j], numSorted[k]]))
                    j += 1
                    k -= 1
            i += 1
        return list(mySet)

            

            





        

            


