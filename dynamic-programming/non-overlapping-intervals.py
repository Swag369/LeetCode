class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        ret = []
        for i in intervals:
            if not ret or ret[-1][-1] <= i[0]:
                ret.append(i)
            
            else:
                continue
            
        return len(intervals) - len(ret)