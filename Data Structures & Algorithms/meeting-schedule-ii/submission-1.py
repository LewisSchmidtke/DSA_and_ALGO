"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        end_times = []
        heapq.heapify(end_times)

        res = 0

        for inter in intervals:
            start = inter.start
            end = inter.end

            if not end_times:
                heapq.heappush(end_times, end)
                continue
            
            earliest = heapq.heappop(end_times)

            if start < earliest:
                heapq.heappush(end_times, earliest)
            else:
                while end_times and start >= earliest:
                    earliest = heapq.heappop(end_times)
        
                if start < earliest:
                    heapq.heappush(end_times, earliest)
            
            heapq.heappush(end_times, end)
            res = max(res, len(end_times))

                
        res = max(res, len(end_times))
        return res

            