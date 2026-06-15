class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)
        opList = []
        for s in strs:
            counts = [0] * 26
            for x in s:
                counts[ord(x) - 97] += 1
            myMap[tuple(counts)].append(s)
        for key in myMap:
            opList.append(myMap[key])
        return opList




        
        

