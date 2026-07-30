class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0 
        start = 0 
        end = len(heights) - 1
        while start < end:
            if heights[start] <= heights[end]:
                area = heights[start] * (end - start)
                if area > maxarea:
                    maxarea = area
                start += 1
            elif heights[end] < heights[start]:
                area = heights[end] * (end - start)
                if area > maxarea:
                    maxarea = area
                end -= 1
        return maxarea