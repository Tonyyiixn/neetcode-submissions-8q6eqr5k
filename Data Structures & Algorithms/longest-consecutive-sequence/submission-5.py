class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count_max = 0
        for n in num_set:
            if n-1 in num_set:
                continue
            
            length = 0
            while length + n in num_set:
                length += 1
            
            count_max = max(length,count_max)
        
        return count_max