# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''

DFS or BFS

then just popmin lowest value in a different loop until we get the one we wanted

but for optimal, since it is a BST, I will want to go left until i have k nodes

questions, what if we have a duplicate?


in order is left middle right


'''

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node):
            if not node:
                return []
            
            return inorder(node.left) + [node.val] + inorder(node.right)
            
        stack = inorder(root)
        # print(stack)
        return stack[k - 1]

