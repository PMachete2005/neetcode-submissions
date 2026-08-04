import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)
        l = 1 
        r = maximum
        k = float('inf')
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                toadd = math.ceil(p / m)
                hours += toadd
            if hours <= h and m < k:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k

