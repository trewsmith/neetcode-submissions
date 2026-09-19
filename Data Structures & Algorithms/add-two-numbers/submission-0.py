# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        curr = l1
        
        while curr is not None:
            next_node = curr.next  # 1. Save the next node
            curr.next = prev       # 2. Reverse the pointer
            prev = curr            # 3. Move prev forward
            curr = next_node       # 4. Move curr forward
            
        l1h = prev

        prev = None

        curr = l2
        
        while curr is not None:
            next_node = curr.next  # 1. Save the next node
            curr.next = prev       # 2. Reverse the pointer
            prev = curr            # 3. Move prev forward
            curr = next_node       # 4. Move curr forward
            
        l2h = prev 

        num1 = ""
        num2 = ""
        cur1 = l1h
        cur2= l2h
        while cur1: 
            num1 += str(cur1.val)
            cur1 = cur1.next
        while cur2: 
            num2 += str(cur2.val)
            cur2 = cur2.next
        
        sSum = str(int(num1) + int(num2))
        
        head = ListNode(int(sSum[0]))
        cur = head 
        for i in range(len(sSum) - 1):
            cur.next = ListNode(int(sSum[i + 1]))
            cur = cur.next
        cur.next = None 

        prev = None

        curr = head
        
        while curr is not None:
            next_node = curr.next  # 1. Save the next node
            curr.next = prev       # 2. Reverse the pointer
            prev = curr            # 3. Move prev forward
            curr = next_node       # 4. Move curr forward
            
        return prev
        


