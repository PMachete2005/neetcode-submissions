class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        allsum = sum(nums)
        if allsum % 2 == 1:
            return False
        half = allsum/2
        mySet = set()
        mySet.add(0)
        mySet.add(nums[-1])
        for i in range(len(nums) - 2, -1, -1):
            toAdd = []
            for ele in mySet:
                if nums[i] + ele == half:
                    return True
                if nums[i] + ele < half:
                    toAdd.append(nums[i] + ele)
            for ele in toAdd:
                mySet.add(ele)
        print(mySet)
        return False