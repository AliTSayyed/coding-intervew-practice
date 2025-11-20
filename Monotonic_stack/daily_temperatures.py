"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""


class Solution:
    def dailyTemperatures(self, temperatures):
        # initilize return array to 0s, handles cases where there are no temps greater
        ret = [0 for i in range(len(temperatures))]

        stack = []

        # for each temp, add its temp and index to the stack
        # if the incoming temp is a greater than the last temp in the stack
        # update the return index to be the distance (ie how many days) between
        # the incoming index and the index stored int he stack
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, prev_index = stack.pop()
                ret[prev_index] = index - prev_index
            stack.append((temp, index))
        return ret


"""
1. Pattern Recognition
Pattern: Monotonic Stack (Decreasing)
Key Characteristics:
Need to find the "next greater/smaller element" for each element
Looking forward in array for first element meeting a condition
Brute force would be O(n²) with nested loops
Elements processed in order, but need to "remember" previous unresolved elements
Similar Problems:
Next Greater Element I/II (LC 496, 503)
Largest Rectangle in Histogram (LC 84)
Trapping Rain Water (LC 42)
Online Stock Span (LC 901)
Car Fleet (LC 853)
Remove K Digits (LC 402)
2. High-Level Approach
Use a monotonic decreasing stack to track temperatures waiting for a warmer day. As you iterate through temperatures, for each new temperature, pop all smaller temperatures from the stack (they've found their answer) and calculate the day difference. Push the current temperature onto the stack to wait for its warmer day.
3. Step-by-Step Logic
Initialize result array with zeros


WHY: Default answer is 0 (no warmer day found), only update when we find one
Pre-filling handles edge case where stack elements never get popped
Initialize empty stack to store (temperature, index) pairs


WHY: Need temperature to compare, index to calculate distance and update result
Iterate through temperatures with enumeration


WHY: Need both current temperature (for comparison) and index (for distance calculation)
While stack is not empty AND current temp > stack top temperature


WHY: Current temp is the answer for all smaller temps waiting in stack
Monotonic property: stack maintains decreasing temperatures from bottom to top
Pop from stack and calculate day difference


WHY: current_index - previous_index gives days until warmer temperature
Update result array at the popped element's original index
Push current (temperature, index) onto stack


WHY: This temperature is now waiting for its warmer day
Maintains monotonic decreasing property
Return result array


WHY: Contains either 0 (no warmer day) or calculated distances for all indices
4. Key Insights & Edge Cases
What Makes This Work:
Monotonic stack property: Stack maintains temperatures in decreasing order
"Waiting list" concept: Stack holds temperatures that haven't found their warmer day yet
One-pass solution: Each element pushed once, popped at most once = O(n)
Immediate resolution: When a warmer temp arrives, ALL cooler temps in stack get resolved instantly
Important Details:
Store tuples (temp, index) not just indices - need temp for comparison
Use while not if for popping - one temperature can resolve multiple waiting temps
Stack elements from bottom to top: decreasing temperatures (monotonic decreasing)
Pre-initialize result with zeros - elegant handling of unresolved elements
Edge Cases:
Strictly decreasing temperatures: stack fills up, result stays all zeros
Strictly increasing temperatures: stack never grows beyond size 1, immediate resolutions
All same temperature: result is all zeros
Single element: returns [0]
Last element: always 0 (no days after it)
5. Pseudocode
function dailyTemperatures(temperatures):
    n = length of temperatures
    result = array of n zeros
    stack = empty stack  // stores (temperature, index)
    
    for index from 0 to n-1:
        current_temp = temperatures[index]
        
        // Resolve all waiting temperatures smaller than current
        while stack is not empty AND stack.top.temperature < current_temp:
            (prev_temp, prev_index) = stack.pop()
            result[prev_index] = index - prev_index
        
        // Current temp now waits for its warmer day
        stack.push((current_temp, index))
    
    return result
    // Any remaining stack elements stay 0 in result

6. Complexity Analysis
Time Complexity: O(n)
Single pass through n temperatures: O(n)
Each element pushed to stack exactly once: n pushes total
Each element popped from stack at most once: n pops total
Amortized O(1) per element
Total: O(n) for iteration + O(n) amortized for stack operations = O(n)
Space Complexity: O(n)
Result array: O(n) - required for output
Stack: O(n) worst case (strictly decreasing temperatures, all elements remain)
Best case stack: O(1) (strictly increasing temperatures)
Total: O(n)
Why Monotonic Stack vs Brute Force:
Brute Force: For each temp, scan forward until warmer found → O(n²)
Monotonic Stack: Each element touched twice max (push + pop) → O(n)
Key insight: Don't need to check every future element, stack "remembers" unresolved elements efficiently

"""
