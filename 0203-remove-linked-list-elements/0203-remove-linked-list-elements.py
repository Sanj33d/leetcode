# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        dummy.next = head ### mmi

        prev = dummy
        cur = head

        while cur:
            if cur.val == val:
                cur = cur.next
                prev.next = cur
            else:
                prev = prev.next
                cur = cur.next
        
        return dummy.next




        