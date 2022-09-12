class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        cur_sum = 0
        
        for n in nums:
            cur_sum += n
            
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
                
        return max_sum