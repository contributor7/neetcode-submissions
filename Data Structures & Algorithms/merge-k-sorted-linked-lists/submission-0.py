# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
loop through every list to check their current node to track a valid min value

heap?

one way is just to traverse thorugh every nodee and put its value on aheap,
then in a for loop create a linkeedlist with value heappopmin
O(N*M) time complexity
O(M) space complexity

if you want O(1), then you need to use the original lists
so just merge two lists until you get no remaining lists
'''
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        def mergeTwoLists(list1, list2):
            dummy = ListNode()
            tail = dummy
            while list1 and list2:
                if list2.val <= list1.val:
                    tail.next = list2
                    list2 = list2.next
                else:
                    tail.next = list1
                    list1 = list1.next
                tail = tail.next
            tail.next = list1 or list2
            return dummy.next

        def printll(head):
            current = head
            while current:
                print(current.val, end=' -> ')
                current = current.next
            print('None')

        # printll(mergeTwoLists(lists[0], lists[1]))
        for i in range(1, len(lists)):
            lists[0] = mergeTwoLists(lists[0], lists[i])
        
        return lists[0]