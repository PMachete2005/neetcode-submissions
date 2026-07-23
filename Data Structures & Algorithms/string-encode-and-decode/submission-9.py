class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedString = "/"
        for string in strs:
            encodedString += str(len(string))
            encodedString += "/"
            encodedString += string
            encodedString += "/"
        return encodedString
            
    def decode(self, s: str) -> List[str]:
        output = []
        if s[0] == "/" and len(s) == 1:
            return output
        i = 0
        while i < len(s):
            currindex = i + 1
            i += 1
            while s[i] != "/":
                i += 1
            if len(s[currindex:i]) > 1:
                length = int(s[currindex:i])
            else:
                length = int(s[currindex])
            i += 1
            output.append(s[i:i + length])
            i += length
            if i + 1 >= len(s):
                return output



       
            