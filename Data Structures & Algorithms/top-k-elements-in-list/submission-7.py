class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap1 = {}
        for n in nums:
            if n in myMap1:
                myMap1[n] += 1
            else:
                myMap1[n] = 1
        myMap2 = defaultdict(list)
        for key in myMap1:
            myMap2[myMap1[key]].append(key)
        length = len(nums)
        output = []
        while length > 0 and len(output) < k:
            if length in myMap2:
                for n in myMap2[length]:
                    output.append(n)
            length -= 1
        return output        






        




        


            

            





        
        
        
