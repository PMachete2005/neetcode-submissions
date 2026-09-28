class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0 
        if len(s) == 1:
            return 1
        left = 0  
        visitedset = set()
        visitedset.add(s[left])
        ls = 1
        maxls = 1
        for right in range(1, len(s)):
            if s[right] in visitedset:
                while s[right] in visitedset:
                    visitedset.remove(s[left])
                    ls -= 1
                    left += 1
            ls += 1
            visitedset.add(s[right])
            maxls = max(maxls, ls)
        return maxls
                    

        


            