"""
Runtime: 95 ms
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        tempIntervals = []
        import sys
        startIndex, endIndex = sys.maxsize, 0
        for i, e in enumerate(intervals):
            if not (e.end < newInterval.start or e.start > newInterval.end):
                tempIntervals.append(e)
                startIndex = min(startIndex, i)
                endIndex = max(endIndex, i)
        if tempIntervals:
            newInterval.start = min(tempIntervals[0].start, newInterval.start)
            newInterval.end = max(tempIntervals[-1].end, newInterval.end)
            for _ in range(startIndex, endIndex+1):
                del intervals[startIndex]
            intervals.insert(startIndex, newInterval)
        else:
            intervals.append(newInterval)
            intervals.sort(key=lambda e: e.start)

        return intervals
