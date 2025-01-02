# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # # approach 1 (47ms, 20mb): O(n) but set used
        # sett = set()
        # while head is not None:
        #     if head not in sett:
        #         sett.add(head)
        #     else:
        #         return True
        #     head = head.next
        # return False
        
        # ## approach2 (49ms, 20mb): O(n)
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
        