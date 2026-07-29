# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        tail.next = head
        while tail.next:
            print("c")
            first = tail.next
            second = tail.next
            tempctr = 0 
            while tempctr != k and second:
                tempctr += 1 
                if tempctr == k:
                    print("a")
                    prev = first
                    curr = first.next
                    first.next = second.next
                    while prev != second:
                        temp = curr.next
                        curr.next = prev
                        prev = curr 
                        curr = temp
                    tail.next = second 
                    tail = first
                else:
                    print("b")
                    second = second.next  
            if tempctr != k:
                break
        return dummy.next 
        

        
        
        
        
        
            
        





        
            
        
