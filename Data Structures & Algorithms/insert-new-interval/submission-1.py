class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start,new_end = newInterval
        for index,(start,end)  in  enumerate(intervals):
            if new_end < start:
                res.append([new_start,new_end])
                return res + intervals[index:]
            elif end < new_start:
                res.append([start,end])
            else:
                new_start = min(new_start,start)
                new_end = max(new_end,end)
        res.append([new_start,new_end])

        return res