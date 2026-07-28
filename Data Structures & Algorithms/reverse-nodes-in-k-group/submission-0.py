# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptrlist = []
        ptr = head
        newHead = ListNode()
        tail = newHead
        finalptr = None
        while ptr:
            ptr2 = ptr
            tempctr = 0
            while ptr2:
                tempctr += 1 
                if tempctr == k:
                    ptrlist.append(ptr)
                    ptr = ptr2.next
                    ptr2.next = None
                ptr2 = ptr2.next
            if tempctr != k:
                finalptr = ptr
                ptr = None
        for i in range(len(ptrlist)):
            prev = None 
            curr = ptrlist[i]
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            ptrlist[i] = prev
            tail.next = ptrlist[i]
            while tail.next:
                tail = tail.next
        tail.next = finalptr
        return newHead.next
        

        
        
        
        
        
            
        





        
            
        
