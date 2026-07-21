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
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        first = head
        second_reversed = prev

        while second_reversed:
            first_next = first.next
            second_reversed_next = second_reversed.next

            first.next = second_reversed
            second_reversed.next = first_next

            second_reversed = second_reversed_next
            first = first_next
        return

