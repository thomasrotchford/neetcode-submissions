# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = head
        slow = head
        prev = None
        counter = 0

        while fast and fast.next:

            fast=fast.next
            
            if counter >= n-1:
                prev=slow
                slow=slow.next

            counter+=1

        
        
        if prev:
            prev.next = slow.next
            del slow
            return head

        else:
            return slow.next or None
        