class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set()
        for n in nums:
            if n in mySet:
                continue
            else:
                mySet.add(n)
        mySet2 = set()
        for x in mySet:
            if (x - 1) not in mySet:
                mySet2.add(x)
            else:
                continue
        consecutivetemp = 0
        consecutive = 0
        for x in mySet2:
            temporary = x
            while temporary in mySet:
                temporary += 1
                consecutivetemp += 1
                if temporary not in mySet:
                    if consecutivetemp > consecutive:
                        consecutive = consecutivetemp
                    consecutivetemp = 0
                    break
        return consecutive








        

