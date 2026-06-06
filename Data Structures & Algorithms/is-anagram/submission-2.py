class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        myMap1 = {}
        myMap2 = {}
        for i in range(len(s)):
            if s[i] in myMap1:
                myMap1[s[i]] = myMap1[s[i]] + 1
            else:
                myMap1[s[i]] = 1
        for j in range(len(t)):
            if t[j] in myMap2:
                myMap2[t[j]] = myMap2[t[j]] + 1
            else:
                myMap2[t[j]] = 1
        for key in myMap1:
            if key in myMap2:
                if myMap1[key] == myMap2[key]:
                    continue
                else:
                    return False
            else:
                return False
        return True


