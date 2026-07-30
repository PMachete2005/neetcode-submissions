class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        for t in tokens:
            if t != "+" and t != "/" and t != "*" and t != "-":
                arr.append(t)
            elif t == "+":
                op1 = int(arr.pop())
                op2 = int(arr.pop())
                sums = op1 + op2
                arr.append(sums)
            elif t == "*":
                op1 = int(arr.pop())
                op2 = int(arr.pop())
                sums = op1 * op2
                arr.append(sums)
            elif t == "-":
                op1 = int(arr.pop())
                op2 = int(arr.pop())
                sums = op2 - op1
                arr.append(sums)
            elif t == "/":
                op1 = int(arr.pop())
                op2 = int(arr.pop())
                sums = op2 / op1
                arr.append(sums)
        return int(arr[0])