# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not(list1) and not(list2): 
            return None
        if not(list1) and list2:
            return list2 
        if not(list2) and list1:
            return list1
        head = ListNode(0) 
        cur = head 
        l = list1
        r = list2
        while l and r:
            if l.val <= r.val:
                cur.next = ListNode(l.val)
                l = l.next
            elif r.val <= l.val:
                cur.next = ListNode(r.val)
                r = r.next
            cur = cur.next
        
        while l:
                cur.next = ListNode(l.val)
                l = l.next
                cur = cur.next
        while r: 
              
                cur.next = ListNode(r.val)
                r = r.next
                cur = cur.next
        return head.next
            