# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #recursive solution

        #base case nothing exists
        if not head:

            return None
        
        #keep track of new head
        newHead = head

        #if sub problem exists
        if head.next:
            
            #recurse to end of list (None)
            newHead = self.reverseList(head.next)

            #next node's pointer points to this one
            head.next.next = head
        
        #set end node(always the current) to none
        head.next=None

        #return beginning of list
        return newHead


            
