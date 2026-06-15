class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "/" + s 
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            lenstr = ""
            while s[i] != "/":
                lenstr = lenstr + s[i]
                i += 1
            i += 1
            length = int(lenstr)
            print(length)
            strs.append(s[i: i + length])
            i = i + length 
        return strs



       
            