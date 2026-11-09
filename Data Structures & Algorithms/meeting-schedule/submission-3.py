"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key= lambda x: x.start)
        prior = None
        for inter in intervals:
            if not prior:
                prior = inter.end
                continue
            if inter.start < prior:
                return False
            
            prior = max(prior, inter.end)
        
        return True
