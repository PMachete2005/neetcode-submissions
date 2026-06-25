class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashsum = 0
        for char in s1:
            hashsum += ord(char)
        print("To be found:",hashsum)
        i = 0 
        while i < (len(s2) - len(s1) + 1):
            j = 0
            hashsumtemp = 0
            while j < len(s1):
                hashsumtemp += ord(s2[i + j])
                j += 1
            print("Hashtemp",i, ":", hashsumtemp)
            if(hashsumtemp == hashsum):
                sa = s2[i:i + len(s1)]
                sasorted = sorted(sa)
                sb = sorted(s1)
                if(sasorted == sb):
                    print("FOUND")
                    return True
                else:
                    print("did not work due to not string match")
                    i += 1
            else:
                print("did not work, next")
                i += 1
        return False