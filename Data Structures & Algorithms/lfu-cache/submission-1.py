from collections import OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.keydict = {}
        self.freqmap = defaultdict(OrderedDict)
        self.occupied = 0 
        self.capacity = capacity 
        self.lowestfrequency = 0
        

    def get(self, key: int) -> int:
        if key not in self.keydict:
            return -1
        else:
            toreturn = self.keydict[key][0]
            frequency = self.keydict[key][1]
            self.keydict[key][1] += 1
            del self.freqmap[frequency][key]
            if len(self.freqmap[self.lowestfrequency]) == 0:
                self.lowestfrequency += 1
            self.freqmap[frequency + 1][key] = None
            return toreturn
        print("g", self.freqmap)
        print("g", self.keydict)
        

    def put(self, key: int, value: int) -> None:
        if key in self.keydict:
            self.keydict[key][0] = value
            self.get(key)
        else:
            if self.capacity == 0:
                return 
            if self.occupied < self.capacity:
                self.occupied += 1
                self.freqmap[0][key] = None
                self.keydict[key] = [value, 0]
                self.get(key)
                self.lowestfrequency = 1
            else:
                keytr = self.freqmap[self.lowestfrequency].popitem(last = False)
                del self.keydict[keytr[0]]
                self.freqmap[0][key] = None
                self.keydict[key] = [value, 0]
                self.get(key)
                self.lowestfrequency = 1
        print(self.freqmap)
        print(self.keydict)

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)