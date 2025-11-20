"""
Given an array of meeting time intervals consisting of start and end times [(s1,e1),(s2,e2),...] (si < ei), determine if a person could attend all meetings.

Example 1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:
(0,30), (5,10) and (0,30),(15,20) will conflict
"""


class Solution:
    def can_attend_meetings(self, intervals) -> bool:
        # Write your code here
        if not intervals:
            return True
        intervals.sort()

        # just check if there is a single overlap case
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                return False
        return True


"""
1. Pattern Recognition
Pattern: Interval Overlap Detection (Sort + Linear Scan)
Key Characteristics:
Check if any two intervals overlap
Boolean result (yes/no conflict)
Sorting enables pairwise comparison
Similar Problems:
Meeting Rooms II (LC 253)
Non-overlapping Intervals (LC 435)
Merge Intervals (LC 56)
2. High-Level Approach
Sort intervals by start time, then scan through comparing each interval's start against the previous interval's end. If any start is less than the previous end, there's an overlap and the person cannot attend all meetings.
3. Step-by-Step Logic
Handle empty input → return True (no conflicts possible)
Sort by start time → brings potentially overlapping intervals adjacent
Track previous end time → comparison point for each interval
Check each interval → if start < prevEnd, overlap exists → return False
Update prevEnd → move comparison point forward
Return True → no overlaps found
4. Key Insights & Edge Cases
Key Insights:
Only need to check adjacent intervals after sorting
start >= prevEnd means no overlap (boundary touching is OK)
Early return on first overlap (don't need to count)
Edge Cases:
Empty list: return True (⚠️ your code returns False - this is a bug!)
Single meeting: return True
Boundary touching [1,2], [2,3]: no overlap
Bug in your code:
if not intervals:
    return False  # Should be True - no meetings = no conflicts

5. Pseudocode
function can_attend_meetings(intervals):
    if intervals is empty:
        return True
    
    sort intervals by start time
    prevEnd = intervals[0].end
    
    for each interval from index 1:
        if interval.start < prevEnd:
            return False  // Overlap found
        prevEnd = interval.end
    
    return True  // No overlaps

6. Complexity Analysis
Time Complexity: O(n log n)
Sorting: O(n log n)
Linear scan: O(n)
Space Complexity: O(1) or O(n)
O(1) if in-place sort
O(n) depending on sort implementation

"""
