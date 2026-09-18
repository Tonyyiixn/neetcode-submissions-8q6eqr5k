class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maximum = 0
        while left < right:
            indices = right - left
            height = min(heights[left],heights[right])
            area = indices * height
            maximum = max(area, maximum)
            if height == heights[left]:
                left += 1
            else:
                right -= 1

        return maximum 