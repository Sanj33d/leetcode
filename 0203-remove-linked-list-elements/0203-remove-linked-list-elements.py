# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # bc: (None) - return None
        # op: node != target: join with next node (node.next = rc, then return node) 
            # node == target: don't join with next node (return rc)

        if head == None:
            return head
        elif head.val != val:
            head.next = self.removeElements(head.next, val)
            return head
        else:
            return self.removeElements(head.next, val)





        