from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = defaultdict(int)
        for num in nums:
            nums_count[num] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for num,count in nums_count.items():
            bucket[count].append(num)
        
        res = []
        for count in range(len(bucket)-1,0,-1):
            for num in bucket[count]:
                res.append(num)
                if len(res) == k:
                    return res