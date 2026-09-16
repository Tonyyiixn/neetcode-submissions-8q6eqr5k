class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for n in num_set:
            if n - 1 in num_set:
                continue
            
            length = 1
            while n + length in num_set:
                length += 1
            
        
            max_len = max(length,max_len)
        
        return max_len