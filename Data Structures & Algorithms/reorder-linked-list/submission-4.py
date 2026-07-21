# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # ensure len(first) >= len(second). first = head
        second = slow.next

        # split head in half
        slow.next = None

        # reverse second half
        reversed_second = None
        while second:
            next_node = second.next
            second.next = reversed_second
            reversed_second = second
            second = next_node

        first = head

        while reversed_second:
            first_next = first.next
            first.next = reversed_second
            first = first.next
            reversed_second = reversed_second.next
            first.next = first_next
            first = first.next
        return

