class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0 
        if len(s) == 1:
            return 1
        left = 0
        maxlen = 1
        duptracker = {}
        duptracker[s[left]] = left
        for right in range(1, len(s)):
            if s[right] not in duptracker or duptracker[s[right]] < left:
                maxlen = max(maxlen, right - left + 1)
            else:
                left = duptracker[s[right]] + 1
            duptracker[s[right]] = right
        return maxlen

        


            