# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# can do with queue: first in last out, or just 
# make each current node point to the previous

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        reversed_list = None
        current = head

        while current:
            next = current.next # need to keep track before changing
            # what current points to due to manipulating reversed_list's
            # pointer to current
            temp = reversed_list
            reversed_list = current
            reversed_list.next = temp
            current = next
        
        return reversed_list