# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None: # bc
            return list2
        elif list2 is None: # bc
            return list1
        else:
            if list1.val < list2.val: # op
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else: # op
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
        
        
        # dummy = ListNode()
        # cur = dummy
        # if list1 == None:
        #     return list2
        # elif list2 == None:
        #     return list1

        # while list1 != None and list2 != None:
        #     if list1.val < list2.val:
        #         cur.next = list1
        #         list1 = list1.next
        #     else:
        #         cur.next = list2
        #         list2 = list2.next
        #     cur = cur.next ## mmi: mistaken in 2nd practise session
        
        # if list1 == None and list2 != None:
        #     cur.next = list2
        # elif list2 == None and list1 != None:
        #     cur.next = list1

        # return dummy.next
        

