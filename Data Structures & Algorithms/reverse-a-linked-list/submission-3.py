# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev=None
        curr=head

        while curr:

            #save next node
            node=curr.next

            #update next ptr to point at previous position
            curr.next=prev

            #update previous to be current address
            prev=curr

            #update current to next node
            curr=node

        #return previous address since current will pass out of scope
        return prev

        