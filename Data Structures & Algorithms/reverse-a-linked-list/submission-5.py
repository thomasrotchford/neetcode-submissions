# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:

            #save pointer that is about to be overwritten
            temp = curr.next 

            #reverse node's pointer
            curr.next = prev 

            #update previous pointer for next loop
            prev = curr

            #move to next node
            curr = temp

        #last node traversed to will be new head to return that
        #curr passes out of scope so return previous
        return prev






        
        