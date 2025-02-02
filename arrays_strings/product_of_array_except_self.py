class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        pre = [1]
        post = [0] * len(nums)
        post[-1] = 1

        for i in range(1, len(nums)):
            pre.append(nums[i - 1] * pre[i - 1])

        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]

        return [pre[i] * post[i] for i in range(len(nums))]
