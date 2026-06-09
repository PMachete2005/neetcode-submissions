import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        outputList = [0] * k
        for i in nums:
            if i in myMap:
                myMap[i] += 1
            else:
                myMap[i] = 1
        myMap2 = defaultdict(list)
        for key,val in myMap.items():
            myMap2[val].append(key)
        outputList = []
        key = len(nums)
        while len(outputList) < k and key >= 0:
            if myMap2[key]:
                outputList.extend(myMap2[key])
            key = key - 1
        return outputList





        
        
        
