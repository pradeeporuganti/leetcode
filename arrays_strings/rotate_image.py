class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for index, check in enumerate(zip(*matrix)):
            matrix[index] = list(check)
            matrix[index].reverse()