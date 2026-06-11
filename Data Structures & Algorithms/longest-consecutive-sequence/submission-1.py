class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myMap = {}
        mySet = set()
        minimum = 10000000000
        for n in nums:
            if n in mySet:
                continue
            else:
                if minimum > n:
                    minimum = n
                mySet.add(n)
        consecutivetemp = 0
        consecutive = 0
        mintemp = minimum
        while mintemp in mySet:
            mintemp += 1
            consecutivetemp += 1
            if mintemp not in mySet:
                if consecutivetemp > consecutive:
                    consecutive = consecutivetemp
                    consecutivetemp = 0
                else:
                    consecutivetemp = 0 
                temp = 10000000000
                for x in mySet:
                    if x > mintemp and x < temp:
                        temp = x
                mintemp = temp
        return consecutive

















        

