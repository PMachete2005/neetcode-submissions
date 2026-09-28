class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.occupied = 0
        self.cache = {}
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right
        node.prev.next = node

    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return
        nn = ListNode(key, value)
        if self.occupied < self.cap:
            self.insert(nn)
            self.cache[key] = nn
            self.occupied += 1
        else:
            toremove = self.left.next
            self.remove(toremove)
            del self.cache[toremove.key]
            self.insert(nn)
            self.cache[key] = nn
  
        
