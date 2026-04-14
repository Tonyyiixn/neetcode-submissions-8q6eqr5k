class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_v = 0
        while l < r:
            height = min(heights[l],heights[r])
            length = r - l
            area = height * length
            if area > max_v:
                max_v = area
            if height == heights[l]:
                l += 1
            elif height == heights[r]:
                r -= 1
            
        return max_v
            
