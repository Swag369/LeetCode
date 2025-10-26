class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        ret = []
        for i in intervals:
            if not ret:
                ret.append(i)
            if ret[-1][-1] <= i[0]:
                if ret[-1][-1] > i[-1]:
                    ret.pop()
                    ret.append(i)
                else:
                    ret.append(i)

            
        return len(intervals) - len(ret)