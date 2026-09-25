# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        startPtr = head
        slow = head
        fast = head.next

        #find ind before median
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        endPtr = None

        #remove middle from second half of list
        cut = slow.next
        slow.next = None
        slow = cut

        #reverse
        while slow:
            tmp = slow.next
            slow.next = endPtr
            endPtr = slow
            slow = tmp
        
        #merge
        while endPtr:

            tmp = startPtr.next
            
            startPtr.next = endPtr

            tmp2 = endPtr.next

            startPtr = tmp

            endPtr.next = tmp

            endPtr = tmp2
