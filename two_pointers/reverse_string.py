class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1

        while r > l:
            s[r], s[l] = s[l], s[r]
            r -= 1
            l += 1

        return s