"""
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.
You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.

Example 1:
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]
Time from [1,1] to [3,4] = 3 seconds
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds

"""


class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sec = 0
        x1, y1 = points.pop()
        while len(points) > 0:
            x2, y2 = points.pop()
            steps = max(abs(x2 - x1), abs(y2 - y1))
            sec += steps
            x1 = x2
            y1 = y2
        return sec


"""
Essentially this question is very wordy but the solution is pretty simple. It's not really about finding the best path. It's about a consistent way of finding the fewest moves to get to the next node. 
The reality is moving diagonally will be the fastest way to traverse until you are within one unit of the point. Then you move 1 unit in the x or y direction to get to that point. Well no matter how far two points are from each other,
The least amount of steps it takes to go from one point to the other IS the greatest difference between either the x or y coordinates. You can never get fewer steps than that. Each step is one second. Return seconds. O(N).
"""
