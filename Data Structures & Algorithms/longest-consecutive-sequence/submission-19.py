class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        mySet = set()
        for n in nums:
            mySet.add(n)
        ctr = 1
        tempctr = 0
        for ele in mySet:
            if ele - 1 in mySet:
                continue
            else:
                tocheck = ele
                while tocheck in mySet:
                    tocheck += 1
                    tempctr += 1
                if tempctr > ctr:
                    ctr = tempctr
                tempctr = 0
        return ctr

      













        

