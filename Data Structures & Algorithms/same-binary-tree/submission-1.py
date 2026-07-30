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
        if p.val != q.val:
            return False
            
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
