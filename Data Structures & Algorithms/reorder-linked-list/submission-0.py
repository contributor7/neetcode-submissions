# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        if not head.next:
            return head
        # if not head or not head.next:
        #   return

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reversed_list = None
        while slow:
            next_node = slow.next
            temp = reversed_list
            reversed_list = slow
            reversed_list.next = temp
            slow = next_node

        # def print_linked_list(head):
        #     current = head
        #     while current:
        #         print(current.val, end=' -> ')
        #         current = current.next
        #     print('None')
        # print_linked_list(reversed_list)
        
        while reversed_list and reversed_list.next:
            reversed_list_next = reversed_list.next
            next_node = head.next
            head.next = reversed_list
            head = head.next
            head.next = next_node
            head = head.next
            reversed_list = reversed_list_next
        return

