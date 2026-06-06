class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        mySet = set()
        ctrs = 0
        ctrt = 0
        for i in range(len(s)):
            if s[i] in mySet:
                continue
            else:
                mySet.add(s[i])
                for j in range(len(s)):
                    if s[j] == s[i]:
                        ctrs = ctrs + 1
                for k in range(len(t)):
                    if t[k] == s[i]:
                        ctrt = ctrt + 1
                if ctrt == ctrs:
                    continue
                else:
                    return False
        return True



