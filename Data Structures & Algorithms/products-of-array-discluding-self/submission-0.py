class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        opList = []
        nonzeroprod = 1
        wzeroprod = 1
        zcounter = 0
        for n in nums:
            if n == 0:
                zcounter += 1
                wzeroprod = wzeroprod * n
            else:
                wzeroprod = wzeroprod * n
                nonzeroprod = nonzeroprod * n
        for n in nums:
            if n == 0:
                if (zcounter - 1) == 0:
                    opList.append(nonzeroprod)
                else:
                    opList.append(0)
            else:
                opList.append(wzeroprod // n)
        return opList 


