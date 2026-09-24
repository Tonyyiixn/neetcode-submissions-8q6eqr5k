class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count_max = 0
        for n in num_set:
            if n - 1 in num_set:
                continue
            
            length = 0
            while n + length in num_set:
                length += 1
            
            count_max = max(count_max,length)
           

        return count_max
