class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        myMap = {}
        left = 0 
        length = 1
        myMap[s[left]] = 0
        right = left + 1 
        while right < len(s):
            if s[right] in myMap:
                length = max(length, right - left)
                left = max(left, myMap[s[right]] + 1)
                myMap[s[right]] = right
            else:
                myMap[s[right]] = right
            right += 1
        length = max(length, (right - left))
        return length