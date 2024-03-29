class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        
        left = 0
        right = len(height) - 1
        
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            res = max(water, res)
            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
        
        return res