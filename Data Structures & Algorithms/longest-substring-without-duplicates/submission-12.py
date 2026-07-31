class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0 
        right = 1
        mySet = set()
        mySet.add(s[left])
        length = 1
        templen = 1
        while right < len(s):
            if s[right] in mySet:
                print("a")
                if templen > length:
                    length = templen
                while s[right] in mySet:
                    print("c")
                    mySet.remove(s[left])
                    left += 1
                templen = right - left
            else:
                print("b")
                templen += 1
                mySet.add(s[right])
                right += 1
        if templen > length:
            length = templen 
        return length 

