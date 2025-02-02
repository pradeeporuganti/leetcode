class Solution:
    def isPalindrome(self, s: str) -> bool:

        # s = "".join(c.lower() for c in s if c.isalnum())
        # return s == s[::-1]

        # above solution is O(n) space

        l, r = 0, len(s) - 1

        while r > l:

            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() == s[r].lower():
                    r -= 1
                    l += 1
                else:
                    return False
            elif (not s[l].isalnum()) and (not s[r].isalnum()):
                r -= 1
                l += 1
            elif not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1

        return True
