# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None: # bc1 (traversal ends, so return None)
            return head 
        elif head.val == val: # bc2 (val matched, so return the next node wo joining cur node)
            return self.removeElements(head.next, val)
        else:                 # update (join the next node with cur node)
            head.next = self.removeElements(head.next, val)

        return head




        