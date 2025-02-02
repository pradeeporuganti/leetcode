class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        p1, p2 = 0, 0

        while p1 < len(s) and p2 < len(t):
            # if both letters are same, increase p1 by 1
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1

        # if a letter towards the end of t shows up first in s, p1 should be less than len(s)
        # if the letter shows up sequentially, p1 is incremented and should be equalt to len(s)
        return p1 == len(s)