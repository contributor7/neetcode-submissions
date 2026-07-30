# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        if not root:
            return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        #iterative DFS
        stack = [root]
        depth = 0

        while stack:
            for _ in range(len(stack)):
                node = stack.pop()

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            depth += 1

        return depth