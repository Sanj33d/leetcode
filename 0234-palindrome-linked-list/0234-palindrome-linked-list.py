# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.cur = head ## oop property must be self mentioned
        def helper(h):
            if h is None: # basecase 1 [hits after entire traversal]
                return True
            else:
                switch = helper(h.next) and h.val == self.cur.val
                self.cur = self.cur.next
                return switch
        
        return helper(head) ## oop nested function doesn't need to be self mentioned


        