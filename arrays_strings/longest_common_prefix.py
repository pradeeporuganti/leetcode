class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        result = []

        for check in zip(*strs):
            if all(element == check[0] for element in check):
                result.append(check[0])
            else:
                break

        return "".join(result)



