"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        ptr = head 
        myMap = {}
        while ptr:
            newNode = Node(ptr.val)
            myMap[ptr] = newNode
            ptr = ptr.next 
        cur = head 
        while cur:
            copy = myMap[cur]
            if cur.next == None:
                copy.next = None 
            else:
                copy.next = myMap[cur.next]
            if cur.random == None:
                copy.random = None 
            else:
                copy.random = myMap[cur.random]
            cur = cur.next
        newHead = myMap[head]
        return newHead

        