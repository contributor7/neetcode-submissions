# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
UPI
U: merge values from a list to the other when the next value of the list being current_merged to is less than the current
    value of the other list
    consider when one list ends (shorter length than the other)

    both lists are already sorted
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if list1 is None and list2 is None:
        #     return None
        # if list1 is None and list2:
        #     return list2
        # elif list2 is None and list1:
        #     return list1
        # can return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # merged = ListNode()
        # current = list1
        # while current and list2.next:
        #     if current.next:
        #         if current.next 


        head = ListNode()
        current_merged = head
        current1 = list1
        current2 = list2
        if current1.val == current2.val:
            current_merged.val = current1.val
            current_merged.next = ListNode(current1.val)
            current_merged = current_merged.next
            current1 = current1.next
            current2 = current2.next
        elif current1.val < current2.val:
            current_merged.val = current1.val
            current1 = current1.next
        else:
            current_merged.val = current2.val
            current2 = current2.next

        while current1 and current2:
            if current1.val == current2.val:
                current_merged.next = ListNode(current1.val)
                current_merged = current_merged.next
                current_merged.next = ListNode(current1.val)
                current1 = current1.next
                current2 = current2.next

            elif current1.val < current2.val:
                current_merged.next = current1
                current1 = current1.next
            else:
                current_merged.next = current2
                current2 = current2.next
            current_merged = current_merged.next
        if not current2 and current1:
            current_merged.next = current1
        elif current2 and not current1:
            current_merged.next = current2
        return head            