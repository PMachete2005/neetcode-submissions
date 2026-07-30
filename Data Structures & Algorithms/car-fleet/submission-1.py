class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position, speed)]
        pairs = sorted(pairs)
        stack = []
        for i in range(len(pairs)):
            if stack:
                stack.append(pairs[-1 - i])
                p1 = stack.pop()
                p2 = stack.pop()
                toreachp1 = (target - p1[0]) / p1[1]
                toreachp2 = (target - p2[0]) / p2[1]
                if toreachp1 <= toreachp2:
                    stack.append(p2)
                else:
                    stack.append(p2)
                    stack.append(p1)
            else:
                stack.append(pairs[-1 - i])
        return len(stack)
