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
        newHead = myMap[head]
        for key in myMap:
            if key.next == None:
                myMap[key].next = None 
            else:
                myMap[key].next = myMap[key.next]
            if key.random == None:
                myMap[key].random = None
            else:
                myMap[key].random = myMap[key.random]
        return newHead
        