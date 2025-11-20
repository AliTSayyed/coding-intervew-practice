"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
"""


class Solution:
    def insert(self, intervals, newInterval):
        res = []

        i, n = 0, len(intervals)

        # check 3 cases
        # if the interval is before the incoming interval, just append it and the rest of the intervals
        # if the interval is after the incoming interval, append the incoming interval
        # if the intervals overlap, merge them via min max operations
        while i < n:
            if newInterval[1] < intervals[i][0]:
                break
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
            i += 1

        res.append(newInterval)

        return res + intervals[i:]


"""
1. Pattern Recognition
Pattern: Interval Merging / Linear Scan with Three Cases
Key Characteristics:
Working with intervals (start/end pairs)
Need to merge overlapping intervals
Input is pre-sorted by start time
Single pass possible due to sorted nature
Three distinct relationships: before, after, overlapping
Similar Problems:
Merge Intervals (LC 56)
Meeting Rooms I/II (LC 252, 253)
Non-overlapping Intervals (LC 435)
Interval List Intersections (LC 986)
Employee Free Time (LC 759)
My Calendar I/II/III (LC 729, 731, 732)
2. High-Level Approach
Process intervals in three phases based on their relationship to newInterval: (1) add all intervals that come completely before newInterval, (2) merge all intervals that overlap with newInterval by continuously updating newInterval's boundaries, (3) add the merged newInterval and append all remaining intervals that come after. This works because the input is pre-sorted, allowing a single left-to-right pass.
3. Step-by-Step Logic
Initialize empty result array and index pointer


WHY: Build result incrementally; track position in original intervals
Iterate through intervals with three-case logic


WHY: Each interval has exactly one relationship to newInterval
Case 1: Current interval ends before newInterval starts


Condition: intervals[i][1] < newInterval[0]
Action: Add current interval to result
WHY: No overlap possible, interval comes completely before
Example: [1,2] vs newInterval [5,7] → keep [1,2]
Case 2: Current interval starts after newInterval ends


Condition: intervals[i][0] > newInterval[1]
Action: Break out of loop
WHY: Found first interval after newInterval; no more overlaps possible (since sorted)
All remaining intervals come after, can append at end
Case 3: Intervals overlap


Condition: Neither case 1 nor case 2 (overlap exists)
Action: Merge by updating newInterval bounds
newInterval[0] = min(newInterval[0], intervals[i][0])
newInterval[1] = max(newInterval[1], intervals[i][1])
WHY: Overlapping intervals must be merged; min/max captures full span
Example: [1,3] + [2,5] → [1,5]
Continue merging all overlapping intervals


WHY: Multiple consecutive intervals might overlap with growing newInterval
newInterval "absorbs" all overlaps as it grows
Add merged newInterval to result


WHY: After loop, newInterval contains all merged overlaps
Position is correct since we processed in order
Append all remaining intervals


Action: res + intervals[i:]
WHY: All remaining intervals come after newInterval (loop broke or finished)
No modifications needed
4. Key Insights & Edge Cases
What Makes This Work:
Pre-sorted input: Enables single pass, no need to sort or look backwards
Three exhaustive cases: Every interval relationship is covered
In-place merging: Update newInterval directly instead of creating intermediate intervals
Break optimization: Once we find first interval after newInterval, we're done processing
Slice efficiency: Python's intervals[i:] efficiently adds remaining intervals
Important Details:
Use min/max for merging - handles all overlap scenarios correctly
Break when finding first "after" interval - no need to process rest
newInterval gets updated during merging - becomes the merged result
Must append newInterval before adding remaining intervals
Don't modify original intervals array (problem allows new array)
Edge Cases:
newInterval before all intervals: breaks immediately, prepends newInterval
Input: [[3,5],[6,9]], new [1,2] → [[1,2],[3,5],[6,9]]
newInterval after all intervals: loop completes, appends at end
Input: [[1,2],[3,5]], new [6,7] → [[1,2],[3,5],[6,7]]
newInterval overlaps all intervals: merges everything into one
Input: [[1,2],[3,5],[6,9]], new [0,10] → [[0,10]]
newInterval overlaps multiple consecutive intervals
Input: [[1,2],[3,5],[6,7]], new [2,6] → [[1,7]]
Empty intervals array: returns [newInterval]
newInterval exactly matches existing: merges into one
5. Pseudocode
function insert(intervals, newInterval):
    result = []
    i = 0
    n = length of intervals
    
    while i < n:
        current = intervals[i]
        
        // Case 1: Current interval is completely before newInterval
        if current.end < newInterval.start:
            result.append(current)
        
        // Case 2: Current interval is completely after newInterval
        else if current.start > newInterval.end:
            break  // Done processing overlaps
        
        // Case 3: Intervals overlap - merge them
        else:
            newInterval.start = min(newInterval.start, current.start)
            newInterval.end = max(newInterval.end, current.end)
        
        i += 1
    
    // Add the merged newInterval
    result.append(newInterval)
    
    // Add all remaining intervals (they come after newInterval)
    result.extend(intervals[i:])
    
    return result

6. Complexity Analysis
Time Complexity: O(n)
n = number of intervals
Single pass through all intervals: O(n)
Each interval examined exactly once
All operations (append, min/max, comparison) are O(1)
Slice operation intervals[i:] is O(n-i) but happens once
Total: O(n)
Space Complexity: O(n)
Result array stores up to n+1 intervals in worst case
Worst case: no merging, newInterval added as separate interval
Best case: O(1) extra space if all intervals merge into one
Space for output doesn't count in auxiliary space, but problem requires new array
If counting output: O(n), if not counting output: O(1) auxiliary space
Why This Works Better Than Alternatives:
Sorting approach: Would need O(n log n) to sort after inserting
Binary search + merge: O(log n) to find position + O(n) to merge = O(n) but more complex
This approach: O(n) single pass, simple three-case logic, leverages pre-sorted input optimally
"""
