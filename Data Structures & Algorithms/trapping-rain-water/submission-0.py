class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left = height[left]
        max_right = height[right]
        water = 0
        while left < right:
            if max_left <= max_right:
                left += 1
                if max_left - height[left] > 0:
                    water += max_left - height[left]
                max_left = max(max_left, height[left])
            else:
                right -= 1
                if max_right - height[right] > 0:
                    water += max_right - height[right]
                max_right = max(max_right, height[right])

        return water

