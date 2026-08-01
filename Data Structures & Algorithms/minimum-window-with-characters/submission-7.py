class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        left = 0 
        minlength = float('inf')
        minstr = ""
        sMap = {}
        tMap = {}
        for i in range(len(t)):
            if t[i] in tMap:
                tMap[t[i]] += 1 
            else:
                tMap[t[i]] = 1
            if s[i] in sMap:
                sMap[s[i]] += 1
            else:
                sMap[s[i]] = 1
        matches = 0 
        for ele in tMap:
            if ele in sMap and tMap[ele] <= sMap[ele]:
                matches += 1
        if matches == len(tMap):
            return s[left:left + len(t)]
        right = left + len(t)
        while right < len(s):
            if s[right] in sMap:
                sMap[s[right]] += 1
            else:
                sMap[s[right]] = 1
            if s[right] in tMap:
                if tMap[s[right]] == sMap[s[right]]:
                    matches += 1
            if matches == len(tMap):
                while matches == len(tMap):
                    if s[left] in tMap and (sMap[s[left]] - 1) < tMap[s[left]]:
                        if len(s[left:right + 1]) < minlength:
                            minlength = len(s[left:right + 1])
                            minstr = s[left:right + 1]
                        matches -= 1
                    sMap[s[left]] -= 1
                    left += 1
            right += 1 
        return minstr
            