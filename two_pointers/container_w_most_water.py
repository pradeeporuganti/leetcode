class Solution:
    def maxArea(self, height: list[int]) -> int:

        max_area = 0
        l, r = 0, len(height) - 1

        while r > l:

            max_area = max(max_area, min(height[r], height[l]) * (r - l))

            # keep taller and move the other
            if height[r] > height[l]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1

        return max_area

