# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # edge case one list is empty
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            temp = ListNode()
            head = temp

            while list1 and list2:
                while list1 and list2 and list1.val == list2.val:
                    temp.val = list1.val

                    temp.next = ListNode(list2.val, ListNode())if list1.next or list2.next else ListNode(list2.val, None)

                    temp = temp.next

                    temp = temp.next

                    
                    list1 = list1.next
                    
                    list2 = list2.next

                while list1 and list2 and list1.val < list2.val:
                    temp.val = list1.val

                    temp.next = ListNode() if list1 or list2 else None
                    temp = temp.next
                    
                    list1 = list1.next

                while list1 and list2 and list2.val < list1.val:
                    temp.val = list2.val

                    temp.next = ListNode() if list1 or list2 else None
                    temp = temp.next
                    
                    list2 = list2.next
            
            while list1:
                    temp.val = list1.val

                    temp.next = ListNode() if list1.next else None
                    temp = temp.next
                    
                    list1 = list1.next

            while list2:
                temp.val = list2.val

                temp.next = ListNode() if list2.next else None
                temp = temp.next
                    
                list2 = list2.next
            
            
            return head
