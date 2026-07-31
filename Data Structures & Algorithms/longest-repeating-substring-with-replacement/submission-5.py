class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myMap = {}      
        left = 0
        currmax = 0
        for right in range(len(s)):
            if s[right] in myMap:
                myMap[s[right]] += 1
            else:
                myMap[s[right]] = 1     
            while (right - left) + 1 - myMap[self.mostfrequentinmap(myMap)] > k:
                myMap[s[left]] -= 1
                left += 1
            currmax = max((right - left) + 1, currmax)
        return currmax

    def mostfrequentinmap(self, myMap: dict[str, int]) -> str:
        maxstr = "A"
        maxcnt = 0
        for ele in myMap:
            if myMap[ele] > maxcnt:
                maxstr = ele
                maxcnt = myMap[ele]
        return maxstr

