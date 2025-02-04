class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        max_sum = sum(nums[:k])
        curr = max_sum

        for i in range(k, len(nums)):
            curr = curr + nums[i] - nums[i - k]

            if curr > max_sum:
                max_sum = curr

        return max_sum / k