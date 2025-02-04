class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        min_length = float('inf')
        l = 0
        running_sum = 0

        for r in range(len(nums)):

            running_sum += nums[r]

            while running_sum >= target:
                min_length = min(min_length, (r - l) + 1)
                running_sum -= nums[l]
                l += 1

        if min_length == float('inf'):
            return 0
        else:
            return min_length

