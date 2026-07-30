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

        # if arr_subroot in arr_root: # does not work
        #     return True
        # return False
        n, m = len(arr_root), len(arr_subroot)

        for i in range(n):
            if arr_root[i] == arr_subroot[0]:
                seen_i = i
                j = 0
                while j < m and seen_i < n:
                    if arr_root[seen_i] != arr_subroot[j]:
                        break
                    seen_i += 1
                    j += 1
                if j == m:
                    return True
            i += 1
        return False

