class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, interval in enumerate(intervals):
            start_pos = newInterval[0]
            end_pos = newInterval[1]
            if end_pos < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif start_pos > interval[1]:
                res.append(interval)
            else:
                newInterval = [min(start_pos, interval[0]), max(end_pos, interval[1])]
        res.append(newInterval)
        return res