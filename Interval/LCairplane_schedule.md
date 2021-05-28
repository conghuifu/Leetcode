### Solution
```
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
            schedules = []
            res = 0

            for i in airplanes:
                schedules.append((i.start, 1))
                schedules.append((i.end, -1))
            schedules.sort()

            cnt = 0
            for i, v in schedules:
                if v == 1:
                    cnt += 1
                else: 
                    cnt -= 1
                res = max(res, cnt)
            return res
```