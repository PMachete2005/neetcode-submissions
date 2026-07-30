class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1 
        maxL = height[left]
        maxR = height[right]
        trappedheight = 0
        while left < right:
            if maxL <= maxR:
                left += 1
                currheight = min(maxL, maxR) - height[left]
                if currheight > 0:
                    trappedheight += currheight
                if height[left] > maxL:
                    maxL = height[left]
            else:
                right -= 1 
                currheight = min(maxL, maxR) - height[right]
                if currheight > 0:
                    trappedheight += currheight
                if height[right] > maxR:
                    maxR = height[right]
        return trappedheight


        

            