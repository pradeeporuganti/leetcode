class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        min_num = float('inf')
        for num in nums:
            if abs(num) < abs(min_num):
                min_num = num
            elif abs(num) == abs(min_num):
                min_num = max(num, min_num)

        return min_num