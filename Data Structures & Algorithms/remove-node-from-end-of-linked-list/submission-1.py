# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #First I will find length of linked list
        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next
        print(length)
        if length == 1:
            return None
        tofind = length - n
        if tofind == 0:
            head = head.next
            return head
        ahead = head
        behind = head
        for i in range(tofind):
            behind = ahead
            ahead = ahead.next
        behind.next = ahead.next 
        return head