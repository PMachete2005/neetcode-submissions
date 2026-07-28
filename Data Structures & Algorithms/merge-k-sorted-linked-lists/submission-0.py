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
        for i in range(len(lists)):
            myMap[i] = lists[i]
        print(myMap)
        totallen = 0 
        for ele in myMap:
            ptr = myMap[ele]
            while ptr:
                totallen += 1
                ptr = ptr.next
        print(totallen)
        for i in range(totallen):
            nn = ListNode()
            minimum = float('inf')
            minele = 0
            for ele in myMap:
                if myMap[ele].val < minimum:
                    minimum = myMap[ele].val
                    minele = ele
            myMap[minele] = myMap[minele].next
            if myMap[minele] == None:
                del myMap[minele]
            nn.val = minimum
            print(nn.val)
            head.next = nn
            head = head.next
        newHead = newHead.next
        return newHead
                    
           




            
