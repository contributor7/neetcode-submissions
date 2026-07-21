# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        remove_index = length - n

        if remove_index == 0:
            return head.next
        current = head
        i = 0
        while current:
            if i == remove_index - 1:
                current.next = current.next.next
                return head
            current = current.next
            i += 1
        return head
            