class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        bestindex = 0 
        total = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            print(total)
            if total >= 0:
                continue
            else:
                total = 0
                bestindex = i + 1
            print(bestindex)
        return bestindex


     

        