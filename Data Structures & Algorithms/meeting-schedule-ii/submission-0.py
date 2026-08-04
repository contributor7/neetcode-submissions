"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # algo, if there is a conflict, i need another room and remember when that conflict was'

        time = []
        for interval in intervals:
            time.append((interval.start, 1))
            time.append((interval.end, -1))

        # [(0, 1), (40, -1), (5, 1), (10, -1), (15, 1), (20, -1)]
        time.sort(key=lambda x: (x[0], x[1]))
        # [(0, 1), (5, 1), (10, -1), (15, 1), (20, -1), (40, -1)]
        res = count = 0

        for t in time:
            count += t[1]
            res = max(res, count)

        return res