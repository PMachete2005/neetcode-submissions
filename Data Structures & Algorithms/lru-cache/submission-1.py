class ListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key 
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:
    def __init__(self, capacity: int):
       self.cap = capacity
       self.cache = {}
       self.left, self.right = ListNode(0, 0), ListNode(0, 0)
       self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        node.prev.next = node.next 
        node.next.prev = node.prev
    
    def insert(self, node):
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right
        node.prev.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            newkey = key
            newval = self.cache[key].val
            self.remove(self.cache[key])
            nn = ListNode(newkey, newval)
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
