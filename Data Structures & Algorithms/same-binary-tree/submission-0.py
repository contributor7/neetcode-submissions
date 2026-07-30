# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
UPI:
Input: two trees: p and q
Out: boolean, T or F

Planning:
recursive, where we check each nodes current value
and traverse
can use a stack
edge cases: one tree ends earlier
'''

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        stack = [(p, q)]

        while stack:
            node_p, node_q = stack.pop()

            if not node_p and not node_q:
                continue

            if not node_p or not node_q:
                return False

            if node_q.val != node_p.val:
                return False

            if node_p.left or node_q.left:
                stack.append((node_p.left, node_q.left))

            if node_p.right or node_q.right:
                stack.append((node_p.right, node_q.right))
                
        return True

        
