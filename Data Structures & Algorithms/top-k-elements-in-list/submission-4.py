class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        counts = defaultdict(list)
        for n in nums:
            if n in myMap:
                myMap[n] += 1
            else:
                myMap[n] = 1
        for key, val in myMap.items():
            counts[val].append(key)
        output = []
        key = len(nums)
        while len(output) < k and key >= 0:
            if counts[key]:
                output.extend(counts[key])
            key -= 1
        return output

        




        


            

            





        
        
        
