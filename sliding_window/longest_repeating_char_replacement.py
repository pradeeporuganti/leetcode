class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest = 0
        letters = set(s)

        for letter in letters:
            l = 0
            count = 0
            for r in range(len(s)):

                if s[r] != letter:
                    count += 1

                if count > k:
                    if s[l] != letter:
                        count -= 1
                    l += 1

                longest = max(longest, (r - l) + 1)

        return longest