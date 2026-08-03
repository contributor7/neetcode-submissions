# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
not BST so values do not matter

preorder is parent, all the way left (all the parents otw there), then 
repeat for bottom right
it uses a stack

starts at top: parent, left, right


inorder is a stack as well
but it is the bottom left, then the parent, then the right

starts at bottom: left, parent, right

leets solve it for a 2 child tree first
        1
    2       3
pre: 1, 2, 3
inorder: 2,1,3

        1
    2
3

pre: 1, 2, 3
inorder: 3, 2, 1



so if i were to traverse in reverse i would start at the opposite end,
like for i in range(len(arr), -1, -1)
for val in arr[::-1]:

'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        indices = {val: idx for idx, val in enumerate(inorder)} # what does this do and why does it work
        # print(indices)

        pre_idx = 0 # or can use a self here

        def dfs(l, r):
            if l > r:
                return None
            nonlocal pre_idx
            
            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)
            mid = indices[root_val] # what does this do?
            root.left = dfs(l, mid - 1) # why does this work
            root.right = dfs(mid + 1, r) # why does this work

            return root
        
        return dfs(0, len(inorder) - 1)









