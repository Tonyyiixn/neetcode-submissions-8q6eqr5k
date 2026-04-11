from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dicta = defaultdict(int)
        for n in nums:
            dicta[n] = 0
        
        longest = 0
        for i in dicta.keys():
            curr = i
            if curr - 1 in dicta:
                continue
            while curr in dicta:
                dicta[i] = dicta[i] + 1
                curr += 1
            longest = max(dicta[i],longest)
        
        return longest