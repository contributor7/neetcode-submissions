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
        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.right: # push right for preorder (not needed)
                stack.append((node.right, depth + 1)) # tuple for memory
            if node.left:
                stack.append((node.left, depth + 1))


        return max_depth