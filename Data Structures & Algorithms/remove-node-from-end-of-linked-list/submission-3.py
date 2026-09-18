# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 0 
        cur = head 
        while cur: 
            count += 1 
            cur = cur.next
       
        x = count - n 
        counter = 0  
        cur = head 
        if count == 1 and n == 1:
            return None 
        elif count == 2 and n == 1: 
            head.next = None 
            return head
        elif count == 2 and n == 2: 
            
            return head.next 
        elif count == 3 and n == 3: 
            return head.next

        elif count == n: 
            return head.next
        while counter < x - 1: 
            cur = cur.next 
            counter +=1
        cur.next = cur.next.next 
        return head
