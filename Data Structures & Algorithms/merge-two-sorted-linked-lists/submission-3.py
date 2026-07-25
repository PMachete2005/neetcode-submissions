# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1p = list1
        l2p = list2
        if l1p == None:
            return list2
        elif l2p == None:
            return list1
        if l1p.val <= l2p.val:
            head = list1
        else:
            head = list2
        while l1p and l2p:
            if l1p.next and l1p.next.val <= l2p.val:
                l1p = l1p.next
            elif  l2p.next and l2p.next.val < l1p.val:
                l2p = l2p.next
            else:
                if l1p and l1p.val <= l2p.val:
                    temp = l1p.next
                    l1p.next = l2p
                    l1p = temp
                else:
                    temp = l2p.next 
                    l2p.next = l1p
                    l2p = temp
        return head
            