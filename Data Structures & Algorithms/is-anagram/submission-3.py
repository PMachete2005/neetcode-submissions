class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        myMap1, myMap2 = {}, {}
        for i in range(len(s)):
            myMap1[s[i]] = 1 + myMap1.get(s[i], 0)
            myMap2[t[i]] = 1 + myMap2.get(t[i], 0)
        for key in myMap1:
            if myMap1.get(key) != myMap2.get(key, 0):
                return False
        return True

