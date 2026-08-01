# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''

'''

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        curr = root

        # go left as much as you can, then check the right
        # return back to the parent, check its right and repeat
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

