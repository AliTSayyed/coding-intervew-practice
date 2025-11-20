"""
Problem:
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""


class Solution:
    def largestRectangleArea(self, heights) -> int:
        max_area = 0
        stack = []

        # going to add (height, index) to the stack
        for index, height in enumerate(heights):
            start = index
            # if the new bar height is less than what we have
            # start poping all potential areas
            while stack and height < stack[-1][0]:
                h, j = stack.pop()
                width = index - j
                area = h * width
                start = j
                max_area = max(max_area, area)
            # use start here because a shorter hieght can extend backwards
            # it doesnt actually start at its index
            stack.append((height, start))

        # clear up the remaining values in the stack (can spand from thier index to the entire length of the array)
        n = len(heights)
        while stack:
            h, j = stack.pop()
            width = n - j
            area = width * h
            max_area = max(max_area, area)

        return max_area


"""
1. Pattern Recognition
Pattern: Monotonic Increasing Stack
Key Characteristics:
Need to find maximum area/span where each element can extend
Each bar's rectangle is limited by first shorter bar on left and right
Brute force O(n²) checking all rectangles is too slow
Elements can "extend backwards" until they hit a taller bar
Need to track both height and starting position
Similar Problems:
Maximal Rectangle (LC 85) - 2D version of this problem
Trapping Rain Water (LC 42)
Daily Temperatures (LC 739)
Remove K Digits (LC 402)
Next Greater Element (LC 496)
Car Fleet (LC 853)
2. High-Level Approach
Use a monotonic increasing stack to track bars that can potentially form rectangles. When encountering a shorter bar, pop all taller bars from the stack and calculate their maximum rectangle area (they've hit their right boundary). Track the leftmost position each bar can extend to by updating the start index when popping. After processing all bars, calculate areas for remaining bars in the stack that extend to the end.
3. Step-by-Step Logic
Initialize max_area and empty stack


WHY: Track maximum found; stack stores (height, start_index) pairs
Iterate through each bar with index and height


WHY: Need both to calculate width and maintain positions
Set start = current index


WHY: By default, this bar starts at its own position
Gets updated if we pop taller bars (bar can extend backwards)
While stack not empty AND current height < stack top height


WHY: Current bar is shorter - it's the RIGHT boundary for taller bars in stack
Monotonic increasing property about to be violated, so resolve
Pop taller bars and calculate their rectangle area


WHY: Popped bar's height × width (current_index - popped_start_index)
This is the maximum rectangle using that bar's height
Update start to popped bar's start index


WHY: KEY INSIGHT - Current shorter bar can extend backwards to where the taller bar started
Example: heights [2, 3, 1] - when at 1, it can extend back to index 0
Update max_area if current area is larger


WHY: Track best rectangle found so far
Push (current_height, start) to stack


WHY: This bar hasn't found its right boundary yet
Uses updated start (not index) to remember how far back it extends
After main loop: process remaining bars in stack


WHY: These bars never hit a shorter bar (right boundary = end of array)
Width = total_length - start_index
Each can extend to the very end
Return max_area


WHY: Contains the largest rectangle found
4. Key Insights & Edge Cases
What Makes This Work:
Monotonic increasing stack: Maintains bars in increasing height order
Backwards extension: Shorter bars inherit the start position of popped taller bars
Two boundaries: Each bar's rectangle is bounded by first shorter bar on left (from stack) and right (current iteration)
Deferred calculation: Only calculate area when we know the right boundary (when we hit shorter bar or end)
Important Details:
Store (height, start_index) not (height, current_index) - start can differ from current
Use start = j when popping - this is the "backwards extension" trick
Must clear stack at end - remaining bars extend to array end
Width calculation differs: during iteration use index - j, at end use n - j
Edge Cases:
Single bar: returns its height × 1
All increasing heights: stack fills, cleared at end, each bar limited by its position
All decreasing heights: each bar processed immediately, max is likely first bar
All same height: one calculation at end, area = height × length
Empty array: returns 0 (no iterations)
5. Pseudocode
function largestRectangleArea(heights):
    max_area = 0
    stack = []  // stores (height, start_index)
    n = length of heights
    
    for index from 0 to n-1:
        current_height = heights[index]
        start = index  // default start position
        
        // Pop all bars taller than current (found their right boundary)
        while stack is not empty AND current_height < stack.top.height:
            (h, start_idx) = stack.pop()
            width = index - start_idx
            area = h × width
            max_area = max(max_area, area)
            start = start_idx  // current bar can extend back to here
        
        // Push current bar with updated start position
        stack.push((current_height, start))
    
    // Process remaining bars (they extend to end of array)
    while stack is not empty:
        (h, start_idx) = stack.pop()
        width = n - start_idx
        area = h × width
        max_area = max(max_area, area)
    
    return max_area

6. Complexity Analysis
Time Complexity: O(n)
Single pass through n bars: O(n)
Each bar pushed to stack exactly once: n pushes
Each bar popped from stack at most once: n pops
All stack operations are O(1)
Final cleanup: at most n pops
Total: O(n) amortized - each element touched at most twice
Space Complexity: O(n)
Stack stores at most n bars in worst case
Worst case: strictly increasing heights - all bars remain until end
Example: [1, 2, 3, 4, 5] - stack grows to size 5
Best case: strictly decreasing - stack size stays ~1
No additional data structures needed
Why Monotonic Stack vs Brute Force:
Brute Force: For each bar, expand left and right to find boundaries → O(n²)
Monotonic Stack: Each bar processed once, boundaries determined by stack → O(n)
Key optimization: Don't recompute - stack "remembers" previous bars and their positions

"""
