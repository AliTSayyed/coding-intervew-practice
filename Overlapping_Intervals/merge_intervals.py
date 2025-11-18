"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""


class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        if len(intervals) <= 1:
            return intervals

        # sort the intervals based on the starting number
        ordered_intervals = sorted(intervals, key=lambda interval: interval[0])

        # create new intervals by looping throught original list
        # use the starting interval of the first segment and update the end interval
        # must start by adding the first interval to the return arr
        ret_intervals = []
        ret_intervals.append(ordered_intervals[0])

        # we compare the next interval with the latest interval in the ret arr
        # if that incoming interval is in range, determine the max length of the interval using max function
        for i in range(1, len(ordered_intervals)):
            if ordered_intervals[i][0] <= ret_intervals[-1][1]:
                ret_intervals[-1][1] = max(
                    ret_intervals[-1][1], ordered_intervals[i][1]
                )
            else:
                ret_intervals.append(ordered_intervals[i])

        return ret_intervals


"""
1. Pattern Recognition
Primary Pattern: Interval Merging / Sorting + Greedy
Key Characteristics:
Problem involves overlapping ranges/intervals
Need to consolidate or merge overlapping segments
Question asks about combining, merging, or finding conflicts in intervals
Input is a collection of ranges with start/end points
Similar Problems:
Insert Interval
Meeting Rooms I & II
Non-overlapping Intervals
Minimum Number of Arrows to Burst Balloons
Employee Free Time
2. High-Level Approach
Sort all intervals by their start time to process them in order. Iterate through the sorted intervals, comparing each with the last merged interval—if they overlap, extend the end of the merged interval; otherwise, add the current interval as a new separate interval. This greedy approach ensures we capture all overlaps in a single pass.
3. Step-by-Step Logic
Sort the intervals by start time


WHY: Sorting ensures we encounter potentially overlapping intervals consecutively, making it easy to detect and merge them in one pass
Initialize result with the first interval


WHY: We need a baseline to compare against; the first interval (after sorting) is guaranteed to have the earliest start time
Iterate through remaining intervals (starting from index 1)


WHY: We've already added the first interval, so we process the rest
For each interval, check if it overlaps with the last interval in result


Compare current interval's start with the last merged interval's end
WHY: If current_start ≤ last_end, the intervals overlap or touch (e.g., [1,3] and [3,5])
If overlapping: Extend the last interval's end


Use max(last_end, current_end) to handle cases where current interval is fully contained
WHY: We want the rightmost boundary of all merged intervals (e.g., merging [1,5] and [2,4] gives [1,5], not [1,4])
If not overlapping: Add current interval as new


WHY: No overlap means this is a distinct, separate interval that should remain independent
4. Key Insights & Edge Cases
What Makes This Work:
Sorting transforms a complex O(n²) comparison problem into a linear O(n) merging problem
Greedy approach works because once sorted, we only need to look at the most recent merged interval
Using max() for the end point handles nested intervals elegantly
Implementation Details:
Must modify the last element in the result array directly (using index [-1])
The overlap condition is ≤ not < (intervals touching at a point should merge: [1,3] + [3,5] = [1,5])
Edge Cases:
Empty input → return empty
Single interval → return as-is
All intervals overlap → returns single merged interval
No overlaps → returns original sorted intervals
Interval fully contained in another → handled by max() function
Intervals touching at boundary points (e.g., [1,3], [3,5]) → should merge
5. Pseudocode
function merge(intervals):
    if intervals is empty or has 1 element:
        return intervals
    
    sorted_intervals = sort intervals by start time
    result = [first interval from sorted_intervals]
    
    for each interval from index 1 to end:
        last_merged = result[last index]
        
        if current.start <= last_merged.end:
            // Overlapping: extend the end
            last_merged.end = max(last_merged.end, current.end)
        else:
            // Not overlapping: add as new interval
            result.append(current)
    
    return result

6. Complexity Analysis
Time Complexity: O(n log n)
Sorting dominates: O(n log n)
Single pass through intervals: O(n)
Overall: O(n log n) due to sorting
Space Complexity: O(n)
Sorting may use O(log n) to O(n) depending on implementation (Python's Timsort uses O(n))
Result array stores up to n intervals in worst case (no overlaps)
Overall: O(n) for output storage

"""
