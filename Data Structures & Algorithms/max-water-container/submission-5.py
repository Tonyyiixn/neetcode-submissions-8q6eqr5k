class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        area_max = 0
        while l < r:
            square = (r-l) * min(heights[l],heights[r])
            area_max = max(square, area_max)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return area_max