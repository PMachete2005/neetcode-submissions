class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord("a")] += 1
            myMap[tuple(count)].append(i)
        outputList = []
        for val in myMap.values():
            outputList.append(val)
        return outputList





        
        

