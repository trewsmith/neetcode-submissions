# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not(head):
            return False
        if not(head.next):
            return False
        fastP = head.next
        slowP = head
        while fastP.next and fastP.val != slowP.val:
            if not(fastP.next.next):
                return False
            fastP = fastP.next.next
            slowP = slowP.next
        if (fastP.val == slowP.val):
            return True
        if not(fastP.next):
            return False