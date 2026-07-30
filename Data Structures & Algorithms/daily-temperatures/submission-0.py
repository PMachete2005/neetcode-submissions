class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) >= 1 and temperatures[stack[len(stack) - 1]] < temperatures[i]:
                idx = stack.pop()
                results[idx] = i - idx
            stack.append(i)
        return results
