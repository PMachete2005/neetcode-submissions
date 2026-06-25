class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashsum = 0
        myMapcheck = {}
        for char in s1:
            hashsum += ord(char)
            if char in myMapcheck:
                myMapcheck[char] += 1
            else:
                myMapcheck[char] = 1 
        i = 0 
        while i < (len(s2) - len(s1) + 1):
            j = 0
            hashsumtemp = 0
            while j < len(s1):
                hashsumtemp += ord(s2[i + j])
                j += 1
            if(hashsumtemp == hashsum):
                sa = s2[i:i + len(s1)]
                myMapA = {}
                for char in sa:
                    if char in myMapA:
                        myMapA[char] += 1
                    else:
                        myMapA[char] = 1
                if myMapA == myMapcheck:
                    return True
                else:
                    i += 1
            else:
                i += 1
        return False