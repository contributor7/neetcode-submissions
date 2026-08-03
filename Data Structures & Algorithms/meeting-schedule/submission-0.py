"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        intervals.sort(key=lambda interval: interval.start)

        n = len(intervals)
        for i in range(n):
            if i < n - 2:
                if intervals[i].end > intervals[i + 1].start:
                    return False
        
        return True