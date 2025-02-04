class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        res = []
        st = []
        curr = root

        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            res.append(curr.val)
            curr = curr.right

        min_diff = float('inf')

        for i in range(len(res) - 1):
            min_diff = min(min_diff, res[i + 1] - res[i])

        return min_diff