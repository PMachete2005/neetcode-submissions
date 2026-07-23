class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)
        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord(char) - 97] += 1
            toCheck = tuple(key)
            myMap[toCheck].append(string)
        return list(myMap.values())
           






        
        

