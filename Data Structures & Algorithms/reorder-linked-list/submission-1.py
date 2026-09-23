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

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        endPtr = None

        while slow:
            tmp = slow.next
            slow.next = endPtr
            endPtr = slow
            slow = tmp
            
        while startPtr:

            tmp = startPtr.next
            
            startPtr.next = endPtr

            tmp2 = endPtr.next

            startPtr = tmp

            endPtr.next = tmp

            endPtr = tmp2
