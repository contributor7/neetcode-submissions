# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
DFS
validating BST
left < root < right

pre order stack can keep track of this

cannot have == either since must strictly be > or <
'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, left_val, right_val):
            if not node:
                return True
            
            if not (left_val < node.val < right_val):
                return False
            
            return valid(node.left, left_val, node.val) and valid(node.right, node.val, right_val)

        return valid(root, float('-inf'), float('inf'))

        # below does not work since I do not keep track of previous values

        # if not root:
        #     return True
        # print(root.val)
        
        # if root.left and root.left.val >= root.val:
        #     return False
        # if root.right and root.right.val <= root.val:
        #     print(root.val, root.right.val)
        #     return False

        # return self.isValidBST(root.left) and self.isValidBST(root.right)



