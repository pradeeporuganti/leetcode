class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 1
        visited = set(s[l])

        for r in range(1, len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            longest = max((r-l) + 1, longest)

        return longest
