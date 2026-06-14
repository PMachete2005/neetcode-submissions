class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        start = 0 
        end = len(heights) - 1
        while start < end:
            if ((end - start) * min(heights[end], heights[start])) > maxarea:
                maxarea = (end - start) * min(heights[end], heights[start])
            if heights[start] < heights[end]:
                start += 1 
                continue
            else:
                end -= 1
                continue
        return maxarea