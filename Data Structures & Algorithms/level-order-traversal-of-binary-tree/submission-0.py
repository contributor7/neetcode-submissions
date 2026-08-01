# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
UPI:
edge case: if not root

BFS, queue, use deque, and use a for loop to check len(queue) for each level and iterate per node
to add all of their children before going down a level
.popleft()

Output: nested list, not tuples. of values
'''

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        res = []

        while queue:
            level_size = len(queue)
            level_arr = []

            for _ in range(level_size):
                node = queue.popleft()

                level_arr.append(node.val)
                if node.left: # prompt asks from left to right, so pop left first when using a queue
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_arr)
        return res






