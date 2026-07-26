# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prevl1 = None 
        currl1 = l1
        while currl1:
            temp = currl1.next
            currl1.next = prevl1
            prevl1 = currl1
            currl1 = temp
        string1 = ""
        p1 = prevl1
        while p1:
            string1 += str(p1.val)
            p1 = p1.next
        print(string1)
        prevl2 = None 
        currl2 = l2
        while currl2:
            temp = currl2.next 
            currl2.next = prevl2
            prevl2 = currl2
            currl2 = temp
        string2 = ""
        p2 = prevl2
        while p2:
            string2 += str(p2.val)
            p2 = p2.next
        print(string2)
        finalstring = str(int(string1) + int(string2))
        print(finalstring)
        strlen = len(finalstring)
        head = ListNode()
        ptr = head
        i = 0 
        while i < strlen:
            print(finalstring[strlen - i - 1])
            ptr.val = finalstring[strlen - i - 1]
            i += 1
            if i < strlen:
                ptr.next = ListNode()
                ptr = ptr.next
        return head
