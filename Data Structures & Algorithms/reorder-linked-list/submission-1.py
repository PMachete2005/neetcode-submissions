# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = slow.next 
        #First, we find center of list via the fast and slow pointers
        while fast:
            if fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                fast = None
        print(slow.val)
        prev = None 
        curr = slow.next
        slow.next = None
        while curr:
            print("Curr now is,", curr.val)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        forwardptr = head
        while prev:
            temp = forwardptr.next 
            forwardptr.next = prev
            prev = prev.next 
            forwardptr.next.next = temp 
            forwardptr = temp


        

        


        

        

        
