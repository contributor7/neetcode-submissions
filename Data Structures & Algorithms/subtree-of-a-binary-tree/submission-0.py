# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''

UPI:

Understand:
Input: 2 roots, each of a BT
Out: boolean

Plan:
algo:
flatten both trees
then check if the subroot list is in root list

'''

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def flatten_tree(root):
            if not root:
                return []
            arr = []
            stack = [root]
            while stack:
                node = stack.pop()
                arr.append(node.val)

                if node.right: # preorder, so append right first
                    stack.append(node.right)
                else:
                    arr.append('#')
                if node.left:
                    stack.append(node.left)
                else:
                    arr.append('#')
            return arr
        
        arr_root = flatten_tree(root)
        arr_subroot = flatten_tree(subRoot)
        print(arr_root, arr_subroot)

        # if arr_subroot in arr_root:
        #     return True
        # return False

        for i, val in enumerate(arr_root): # enumerate is index then val
            if val == arr_subroot[0]:
                j = 0
                while j < len(arr_subroot) and i < len(arr_root):
                    if arr_root[i] != arr_subroot[j]:
                        break
                    if j == len(arr_subroot) - 1:
                        return True
                    i += 1
                    j += 1

        return False



