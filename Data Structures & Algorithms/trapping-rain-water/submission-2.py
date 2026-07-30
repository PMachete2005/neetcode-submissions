class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft = [0] * len(height)
        maxright = [0] * len(height)
        for i in range(len(height)):
            if i == 0:
                maxleft[i] = 0
                maxright[len(height) - i - 1] = 0
            else:
                maxleft[i] = max(height[i - 1], maxleft[i - 1])
                maxright[len(height) - i - 1] = max(height[len(height) - i], maxright[len(height) - i])
        trappedheight = 0 
        for i in range(len(height)):
            currheight = min(maxleft[i], maxright[i]) - height[i]
            if currheight > 0:
                trappedheight += currheight
        return trappedheight

        

            