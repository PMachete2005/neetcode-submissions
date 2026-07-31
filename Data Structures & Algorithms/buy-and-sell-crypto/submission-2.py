class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = left + 1
        maxprof = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                curprof = prices[right] - prices[left]
                if curprof > maxprof:
                    maxprof = curprof
                right += 1
        return maxprof


            
            
