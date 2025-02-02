class Solution:
    def romanToInt(self, s: str) -> int:

        ranks = {'I': [1, 1], 'V': [2, 5], 'X': [3, 10], 'L': [4, 50], 'C': [5, 100], 'D': [6, 500], 'M': [7, 1000]}
        result = 0

        i = 0

        while i < len(s):
            if i != len(s) - 1:
                if ranks[s[i]][0] >= ranks[s[i + 1]][0]:
                    result += ranks[s[i]][1]
                    i += 1
                elif ranks[s[i]][0] < ranks[s[i + 1]][0]:
                    result += ranks[s[i + 1]][1] - ranks[s[i]][1]
                    i += 2
            elif i == len(s) - 1:
                result += ranks[s[i]][1]
                i += 1

        return result