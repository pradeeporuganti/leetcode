class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            max_profit = max(max_profit, prices[r] - prices[l])

            if prices[l] <= prices[r]:
                r += 1
            elif prices[l] > prices[r]:
                l = r
                r = l + 1

        return max_profit