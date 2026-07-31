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
            while (right - left) + 1 - max(myMap.values()) > k:
                myMap[s[left]] -= 1
                left += 1
            currmax = max((right - left) + 1, currmax)
        return currmax

