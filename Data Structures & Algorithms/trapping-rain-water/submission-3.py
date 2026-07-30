class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        maxleft = [0] * length
        maxright = [0] * length
        for i in range(length):
            if i == 0:
                maxleft[i] = 0
                maxright[length - i - 1] = 0
            else:
                maxleft[i] = max(height[i - 1], maxleft[i - 1])
                maxright[length - i - 1] = max(height[length - i], maxright[length - i])
        trappedheight = 0 
        for i in range(length):
            currheight = min(maxleft[i], maxright[i]) - height[i]
            if currheight > 0:
                trappedheight += currheight
        return trappedheight

        

            