class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + '/' + s 
        return res
    def decode(self, s: str) -> List[str]:
        opList = []
        i = 0
        while i < len(s):
            ir1 = i
            j = i
            while (j < len(s)) and s[j] != '/':
                j = j + 1
            ir2 = j
            if ir1 == ir2:
                length = int(s[ir1])
            else:
                length = int(s[ir1:ir2])
            startindex = j + 1
            endindex = j + length + 1
            opList.append(s[startindex:endindex])
            i = j + length + 1
        return opList
            