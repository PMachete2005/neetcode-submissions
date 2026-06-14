class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        start = 0 
        end = len(heights) - 1
        while start < end:
            curarea = (end - start) * min(heights[end], heights[start])
            if curarea > maxarea:
                maxarea = curarea
            if heights[start] < heights[end]:
                start += 1 
                continue
            if heights[end] < heights[start]:
                end -= 1
                continue
            if heights[start] == heights[end]:
                start += 1
                continue
        return maxarea