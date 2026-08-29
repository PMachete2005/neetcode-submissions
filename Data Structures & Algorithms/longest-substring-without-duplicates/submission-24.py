class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0 
        if len(s) == 1:
            return 1
        left = 0
        maxlen = 1
        duptracker = set()
        duptracker.add(s[left])
        for right in range(1, len(s)):
            if s[right] not in duptracker:
                maxlen = max(maxlen, right - left + 1)
                print("Len", maxlen)
            else:
                while s[right] in duptracker:
                    duptracker.remove(s[left])
                    left += 1
            duptracker.add(s[right])
        return maxlen

        


            