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
        
        # prev = None
        reversed_list = None
        current = head

        # temp = head
        # temp.next = None

        while current:
            temp = reversed_list
            next = current.next
            reversed_list = current
            reversed_list.next = temp
            # prev = temp
            # reversed_list = reversed_list.next
            current = next
        
        return reversed_list