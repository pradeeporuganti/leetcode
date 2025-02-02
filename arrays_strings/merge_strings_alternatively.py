class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        min_length = min(len(word1), len(word2))
        merged = []

        for i in range(min_length):
            merged.extend([word1[i], word2[i]])

        if len(word1) > len(word2):
            merged.extend(word1[len(word2)::])
        elif len(word1) < len(word2):
            merged.extend(word2[len(word1)::])

        return "".join(merged)