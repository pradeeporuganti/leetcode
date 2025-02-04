from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        window = len(s1)
        counts_s1, counts_s2 = Counter(s1), Counter(s2[0:window])

        if counts_s1 == counts_s2:
            return True

        l, r = 0, window

        while r < len(s2):

            counts_s2[s2[l]] -= 1
            counts_s2[s2[r]] += 1

            if counts_s1 == counts_s2:
                return True

            r += 1
            l += 1

            # if all([s1.count(letter) == check.count(letter) for letter in s1]):
            #     return True

        return False