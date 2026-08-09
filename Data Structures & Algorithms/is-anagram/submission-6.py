class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            myMap = {}
            for char in s:
                if char in myMap:
                    myMap[char] += 1
                else:
                    myMap[char] = 1
            myMap2 = {}
            for chars in t:
                if chars in myMap2:
                    myMap2[chars] += 1 
                else:
                    myMap2[chars] = 1
            if myMap == myMap2:
                return True
            else:
                return False
        
