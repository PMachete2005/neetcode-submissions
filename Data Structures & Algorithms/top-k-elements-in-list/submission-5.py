class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        for n in nums:
            if n in myMap:
                myMap[n] += 1 
            else:
                myMap[n] = 1
        #Now, that we have a map of all elements and their counts
        myMap2 = defaultdict(list)
        for key in myMap:
            myMap2[myMap[key]].append(key)
        i = len(nums)
        output = []
        while i > 0 and len(output) < k:
            if i in myMap2:
                for n in myMap2[i]:
                    output.append(n)
            i -= 1
        return output
            





        




        


            

            





        
        
        
