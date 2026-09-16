from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1

        # buckets[i] = list of numbers that appear exactly i times
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in dic.items():
            buckets[count].append(num)

        # walk from highest count down, collecting until we have k
        res = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                res.append(num)
                if len(res) == k:
                    return res