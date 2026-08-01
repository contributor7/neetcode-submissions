# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''

DFS or BFS

then just popmin lowest value in a different loop until we get the one we wanted

but for optimal, since it is a BST, I will want to go left until i have k nodes

questions, what if we have a duplicate?
'''

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        # O(N) sol:
        def dfs(root):
            if not root:
                return
            stack = [root]
            while stack:
                node = stack.pop()
                values.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        dfs(root)

        heapq.heapify(values)
        # this is O(klogN) time complexity, not ideal
        for i in range(k):
            if i == k - 1:  # k is 1-indexed
                return heapq.heappop(values)
            heapq.heappop(values)

