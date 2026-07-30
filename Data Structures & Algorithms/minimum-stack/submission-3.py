class MinStack:

    def __init__(self):
        self.arr = []
        self.minimum = float('inf')
        self.minarr = []
    def push(self, val: int) -> None:
        self.arr.append(val)
        if val < self.minimum:
            self.minimum = val
            self.minarr.append(len(self.arr) - 1)
    def pop(self) -> None:
        if self.minarr[len(self.minarr) - 1] == (len(self.arr) - 1):
            self.minarr.pop()
            if len(self.minarr) > 0:
                idx = self.minarr[len(self.minarr) - 1]
                self.minimum = self.arr[idx]
            else:
                self.minimum = float('inf')
        self.arr.pop()
    def top(self) -> int:
        return self.arr[len(self.arr) - 1]
    def getMin(self) -> int:
        return self.arr[self.minarr[len(self.minarr) - 1]]
        
