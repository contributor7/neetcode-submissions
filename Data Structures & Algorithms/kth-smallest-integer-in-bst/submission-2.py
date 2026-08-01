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

        # def inorder(node, stack):
        #     # if not stack:
        #     #     stack = []
        #     if len(stack) == k:
        #         # break # or should i do return stack[k -1]?
        #         return stack[k - 1]
                
        #     if not node:
        #         return []
        #     stack = inorder(node, stack)
        #     return inorder(node.left, stack) + [node.val] + inorder(node.right, stack)


        # stack = []
        # print(inorder(root, stack))
        count = k
        res = root.val

        def inorder(node):
            # if len(stack) == k:
            #     return stack[k - 1]
            nonlocal count, res
            
            if not node:
                return

            inorder(node.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                res = node.val
                return
            inorder(node.right)

        inorder(root)
        return res

        # print(stack)
        # return stack[k - 1]

