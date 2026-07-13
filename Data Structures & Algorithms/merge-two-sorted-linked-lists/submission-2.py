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

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        dummy = ListNode()
        merged = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next
            
        if list1:
            merged.next = list1
        else:
            merged.next = list2
        return dummy.next