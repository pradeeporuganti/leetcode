class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]

        ## O(n) space. try 2 pointer approach