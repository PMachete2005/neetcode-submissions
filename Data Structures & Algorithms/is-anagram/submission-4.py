class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sorted_s = self.mergesort(list(s))
        sorted_t = self.mergesort(list(t))
        if sorted_s == sorted_t:
            return True
        else:
            return False
    
    def mergesort(self, s: List) -> List:
        if len(s) <= 1:
            return s
        else:
            mid = len(s)//2
            left = self.mergesort(s[:mid])
            right = self.mergesort(s[mid:])
            return self.merge(left, right)
    def merge(self, l1: List, l2: List) -> List:
        i = 0 
        j = 0
        arr = []
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                arr.append(l1[i])
                i = i + 1
            elif l2[j] < l1[i]:
                arr.append(l2[j])
                j = j + 1
            else:
                arr.append(l1[i])
                i = i + 1
        arr.extend(l1[i:])
        arr.extend(l2[j:])
        return arr
        
