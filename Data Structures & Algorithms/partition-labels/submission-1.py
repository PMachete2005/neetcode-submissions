class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        myMap = {}
        for i in range(len(s)):
            myMap[s[i]] = i
        end = myMap[s[0]]
        size = 0
        output = []
        for i in range(len(s)):
            end = max(end, myMap[s[i]])
            if i != end:
                size += 1
            else:
                size += 1
                output.append(size)
                size = 0
        return output


        






            




        