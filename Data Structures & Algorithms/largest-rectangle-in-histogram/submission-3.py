class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        stack = []
        stack.append([0, heights[0]])
        maxarea = 0 
        i = 1
        while i < len(heights):
            if heights[i] >= stack[-1][1]:
                stack.append([i, heights[i]])
            else:
                index = -1
                while stack and heights[i] < stack[-1][1]:
                    curr = stack.pop()
                    area = (i - curr[0]) * curr[1]
                    index = curr[0]
                    if area > maxarea:
                        maxarea = area
                stack.append([index, heights[i]])
            i += 1
        final = len(heights)
        while stack:
            curr = stack.pop()
            area = (final - curr[0]) * curr[1]
            if area > maxarea:
                maxarea = area
        return maxarea
