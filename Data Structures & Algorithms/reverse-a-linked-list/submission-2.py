# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        
        if not head:

            return head

        else:

            print("in",head,head.val,head.next)
            temp = ListNode(head.val,None)
            print("temp",temp,temp.val,temp.next)
            address = temp
            head = head.next
            

            while head and head.next:
                print("in",head,head.val,head.next)
                temp = ListNode(head.val,address)
                print("temp",temp,temp.val,temp.next)
                address = temp
                head = head.next
            if head:
                print("in",head,head.val,head.next)
                temp = ListNode(head.val,address)
                print("temp",temp,temp.val,temp.next)

            return temp

        