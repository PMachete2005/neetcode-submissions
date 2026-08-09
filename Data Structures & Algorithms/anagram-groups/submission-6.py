class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - 97] += 1
            myMap[tuple(count)].append(s)
        return list(myMap.values())





        
        

