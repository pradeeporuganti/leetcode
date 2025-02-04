# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        q = deque([(root, 1)])
        max_depth = 0

        while q:
            node, depth = q.popleft()
            if node:
                max_depth = max(depth, max_depth)
                q.append((node.left, depth + 1))
                q.append((node.right, depth + 1))

        return max_depth

