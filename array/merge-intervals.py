class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals=sorted(intervals)

        i = 0

        ret = []

        while i < len(intervals):

            if i == 0 or ret[-1][-1] < intervals[i][0]:
                ret.append(intervals[i])
            
            else:
                ret[-1][-1] = max(ret[-1][-1], intervals[i][-1])

            i+=1

        return ret