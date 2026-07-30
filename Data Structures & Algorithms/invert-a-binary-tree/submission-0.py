# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




'''
UPI:

U: flip the right and left subtree
In: root
Out: root

P:

recursive

wrong plan: will need a data structure to store temporary values
algo: change the leaves first, then move up and finally change root.left and root.right
like postorder from right to left

'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root

        