# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        newHead = head
        myMap = {}
        totallen = 0
        for i in range(len(lists)):
            myMap[i] = lists[i]
            ptr = lists[i]
            while ptr:
                totallen += 1
                ptr = ptr.next
        for i in range(totallen):
            minimum = float('inf')
            minele = 0
            for ele in myMap:
                if myMap[ele].val < minimum:
                    minimum = myMap[ele].val
                    minele = ele
            head.next = myMap[minele]
            head = head.next
            myMap[minele] = myMap[minele].next
            if myMap[minele] == None:
                del myMap[minele]
        newHead = newHead.next
        return newHead
                    
           




            
