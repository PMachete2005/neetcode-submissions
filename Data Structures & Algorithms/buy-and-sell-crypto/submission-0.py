class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minindex = 0
        i = minindex + 1 
        profit = 0 
        while i < len(prices):
            if (prices[i] < prices[minindex]):
                minindex = i
                i += 1 
                continue
            else:
                curprof = (prices[i] - prices[minindex])
                if curprof > profit:
                    profit = curprof
                i += 1
                if i == len(prices):
                    break
                else:
                    continue
        return profit
            
            
