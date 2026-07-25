# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mySet = set()
        x = head 
        if x == None:
            return False
        while x.next:
            if x in mySet:
                return True
            else:
                mySet.add(x)
            x = x.next 
        return False
            