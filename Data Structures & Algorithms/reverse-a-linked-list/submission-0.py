# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        regList = []
        curr = head
        if (head == None):
            return None
        while(curr != None):
            regList.append(curr.val)
            curr = curr.next
        regList.reverse()
        
        
        head = ListNode(regList[0])
        curr = head
        

        for num in range(1, len(regList)):
            newNode = ListNode(regList[num])
            curr.next = newNode
            curr = newNode

        return head