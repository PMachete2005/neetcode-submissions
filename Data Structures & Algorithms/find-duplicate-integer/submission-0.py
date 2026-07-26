class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mySet = set()
        for n in nums:
            if n in mySet:
                return n 
            else:
                mySet.add(n)