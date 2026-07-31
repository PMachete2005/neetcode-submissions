class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        left = 0 
        length = 0
        for right in range(len(s)):
            if s[right] in mySet:
                while s[right] in mySet:
                    mySet.remove(s[left])
                    left += 1
            mySet.add(s[right])
            right += 1
            length = max(right - left, length)
        return length


            