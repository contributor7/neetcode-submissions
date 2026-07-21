# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head

        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # prev.next = None

        reversed_list = None
        while slow:
            next_node = slow.next
            temp = reversed_list
            reversed_list = slow
            reversed_list.next = temp
            slow = next_node
        
        while reversed_list and reversed_list.next:
            next_node = head.next
            head.next = reversed_list
            head = head.next
            reversed_list = reversed_list.next
            head.next = next_node
            head = head.next
        return

