class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals.sort(key = lambda i:i[0])
        i = 0
        while i < len(intervals)-1:
            first_interval = intervals[i]
            second_interval = intervals[i+1]
            
            if second_interval[0] <= first_interval[1]:
                f = min(first_interval[0], second_interval[0])
                s = max(first_interval[1], second_interval[1])
                new_interval = [f, s]
                intervals.remove(first_interval)
                intervals.remove(second_interval)
                intervals.insert(i, new_interval)
            else:
                i+=1
        return intervals