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

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = 0
        res = root.val

        def inorder(node):
            # if len(stack) == k:
            #     return stack[k - 1]
            nonlocal count, res

            if not node:
                return

            inorder(node.left)

            count += 1
            if count == k:
                res = node.val
                return
            inorder(node.right)

        inorder(root)
        return res

