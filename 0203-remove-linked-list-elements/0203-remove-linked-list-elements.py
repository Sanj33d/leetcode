# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None: # 1. bc (traversal ends, so return None)
            return head 
        elif head.val == val: # 3. operation (coincidentally rc too: val matched, so return the next node wo joining cur node)
            return self.removeElements(head.next, val)
        else:                 # 2. rc (traversal: join the next node with cur node)
            head.next = self.removeElements(head.next, val)

        return head




        