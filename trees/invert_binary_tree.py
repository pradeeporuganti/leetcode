# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        res = []

        if not root:
            return

        q = collections.deque()
        q.append(root)

        while q:

            node = q.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root



