class MinStack:

    def __init__(self):
        self.arr = []
        self.length = 0
        self.minimum = float('inf')
        self.minarr = []
        self.minindex = 0
        self.minindexlength = 0
    def push(self, val: int) -> None:
        self.arr.append(val)
        self.length += 1
        if val < self.minimum:
            self.minimum = val
            self.minindex = self.length - 1
            self.minarr.append(self.minindex)
            self.minindexlength += 1
    def pop(self) -> None:
        if self.minindex == self.length - 1:
            self.minindex = self.minarr[self.minindexlength - 2]
            self.minimum = self.arr[self.minindex]
            self.minarr.pop()
            self.minindexlength -= 1
        self.arr.pop()
        self.length -= 1
        if len(self.arr) == 0:
            self.minimum = float('inf')
    def top(self) -> int:
        return self.arr[self.length - 1]
    def getMin(self) -> int:
        return self.arr[self.minindex]
        
