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
        second_reversed = None
        while second:
            next_node = second.next
            second.next = second_reversed
            second_reversed = second
            second = next_node

        first = head
        second = second_reversed

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            second = second_next
            first = first_next
        return

