"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        q = deque()
        q.append(node)
        myMap = {}
        toreturn = None
        while q:
            curnode = q.popleft()
            if curnode not in myMap:
                nn = Node()
                nn.val = curnode.val
                myMap[curnode] = nn
            ng = myMap[curnode]
            if ng.val == 1:
                toreturn = ng
            for n in curnode.neighbors:
                if n not in myMap:
                    q.append(n)
                    nn = Node()
                    myMap[n] = nn
                    nn.val = n.val
                ng.neighbors.append(myMap[n])
        return toreturn

            





        