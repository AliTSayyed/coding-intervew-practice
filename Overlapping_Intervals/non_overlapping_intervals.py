"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
"""


class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        ordered_intervals = sorted(intervals, key=lambda interval: interval[0])

        count = 0
        prevEnd = ordered_intervals[0][1]
        # check if the current interval is overlapping another interval
        # if it is, then we consider the shorter ending interval as the next to compare to
        for i in range(1, len(ordered_intervals)):
            start = ordered_intervals[i][0]
            end = ordered_intervals[i][1]
            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1
                prevEnd = min(end, prevEnd)
        return count


"""
1. Pattern Recognition
Pattern: Greedy Interval Scheduling (Sort by End Time)
Key Characteristics:
Maximize/minimize intervals kept/removed
Need to find maximum set of non-overlapping intervals
Classic activity selection problem
Sorting enables greedy choice
Similar Problems:
Meeting Rooms I/II (LC 252, 253)
Minimum Number of Arrows to Burst Balloons (LC 452)
Insert Interval (LC 57)
Merge Intervals (LC 56)
2. High-Level Approach
Sort intervals by end time, then greedily keep intervals that don't overlap with the previously kept interval. Always keeping the earliest-ending interval maximizes room for future intervals. Count removals when overlap occurs.
3. Step-by-Step Logic
Sort by end time


WHY: Earliest-ending intervals leave most room for others
Track previous end time


WHY: Need to compare each interval against last kept interval
For each interval, check overlap


If start >= prevEnd: No overlap → keep it, update prevEnd
If start < prevEnd: Overlap → increment removal count, keep earlier-ending one (already prevEnd)
Return removal count


WHY: Count of intervals that must be removed for non-overlapping set
4. Key Insights & Edge Cases
Key Insights:
Sort by END, not start - greedy choice that maximizes remaining space
No need for min(end, prevEnd) when sorted by end - previous end is always ≤ current end
Keeping earliest-ending interval is always optimal (classic proof by exchange argument)
Edge Cases:
Single interval: return 0
All overlapping: return n-1
No overlaps: return 0
Intervals sharing boundary ([1,2], [2,3]): not overlapping (start >= prevEnd)
5. Pseudocode
function eraseOverlapIntervals(intervals):
    sort intervals by end time
    
    count = 0
    prevEnd = intervals[0].end
    
    for i from 1 to n-1:
        if intervals[i].start >= prevEnd:
            prevEnd = intervals[i].end    // Keep this interval
        else:
            count += 1                     // Remove this interval
    
    return count

6. Complexity Analysis
Time Complexity: O(n log n)
Sorting: O(n log n)
Single pass: O(n)
Total: O(n log n)
Space Complexity: O(1) or O(n)
O(1) if sorting in-place
O(n) if sort creates new array (Python's sorted())

"""
