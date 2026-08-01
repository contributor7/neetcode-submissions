# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
UPI:

BST, will need to compare values
O(h), so use DFS. which uses a stack

constraints: all nodes are unique, p != q, and both p and q exist in the BST

P:
check if p < q?
if so then dfs right subtree of p, both sides. it is possible p is the common ancestor.

but we must start from the root since we need to track the ancestor

if (p.val < root.val and root.val > q.val) or (q.val < root.val and root.val > p.val):
    return root.val
"""


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            if (p.val <= node.val and node.val <= q.val) or (
                q.val <= node.val and node.val <= p.val
            ):
                return node

            if node.right: # preorder
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

