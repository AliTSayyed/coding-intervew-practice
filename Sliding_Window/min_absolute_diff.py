"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

"""


class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """

        # sort the array, only adjacent value are checked since
        # all values are distinct and the minimum difference is only possible by adjacent values (i,e 2-1 = 1 cant get smaller than 1)
        arr.sort()

        # pass over the array and mind the min value
        min_diff = float("inf")
        for i in range(0, len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_diff:
                min_diff = diff

        ret = []
        # check what pairs equal the min diff and add it to the ret array
        for i in range(0, len(arr) - 1):
            diff = arr[i + 1] - arr[i]

            if diff == min_diff:
                ret.append([arr[i], arr[(i + 1)]])

        return ret


"""
1. Pattern Recognition
Pattern: Sort + Adjacent Element Comparison
Key characteristics that indicate this pattern:
Problem asks for "minimum difference" or "closest pair" between elements
Need to compare elements to find smallest gap
Array contains distinct integers (no duplicates to worry about)
Similar problems:
Find pair with minimum sum
Minimum gap in sorted array
K-diff pairs (with specific difference)
Closest pair from two sorted arrays
2. High-Level Approach
Sort the array to bring similar values next to each other. Since we want minimum differences, we only need to check adjacent elements (closest neighbors have the smallest differences). Make two passes: first to find the minimum difference value, then to collect all pairs with that exact difference.
3. Step-by-Step Logic
Sort the array


WHY: Brings similar values together as neighbors; minimum differences will only exist between adjacent elements
After sorting, checking non-adjacent pairs is wasteful (they'll always have larger differences)
First pass - Find minimum difference


Iterate through array checking arr[i+1] - arr[i] for all adjacent pairs
Track the smallest difference found
WHY: We need to know what the target difference is before collecting pairs
Second pass - Collect all pairs matching minimum


Iterate through array again checking adjacent pairs
When arr[i+1] - arr[i] equals the minimum, add [arr[i], arr[i+1]] to result
WHY: There may be multiple pairs with the same minimum difference
Return the collected pairs


Already in ascending order because we processed left-to-right on sorted array
4. Key Insights & Edge Cases
Core insight: In a sorted array of distinct elements, the minimum absolute difference can ONLY occur between adjacent elements
Why adjacent only? If elements are far apart in sorted order, their values are far apart too
No absolute value needed: Since array is sorted, arr[i+1] - arr[i] is always non-negative
No duplicates possible: Each adjacent pair is checked exactly once; distinct elements guarantee no duplicate pairs
Ordering handled automatically: Processing left-to-right on sorted array produces pairs in ascending order
Edge cases:
Array with 2 elements: Only one pair to check
All pairs have same minimum: Return all adjacent pairs
Array already sorted: Still works correctly
5. Pseudocode
function minimumAbsDifference(arr):
    // Step 1: Sort
    sort(arr)
    
    // Step 2: Find minimum difference
    min_diff = infinity
    for i from 0 to length(arr) - 2:
        current_diff = arr[i+1] - arr[i]
        if current_diff < min_diff:
            min_diff = current_diff
    
    // Step 3: Collect all pairs with minimum difference
    result = empty list
    for i from 0 to length(arr) - 2:
        if arr[i+1] - arr[i] == min_diff:
            result.append([arr[i], arr[i+1]])
    
    return result

6. Complexity Analysis
Time Complexity: O(n log n)


Sorting: O(n log n)
First pass to find minimum: O(n)
Second pass to collect pairs: O(n)
Overall dominated by sorting: O(n log n)
Space Complexity: O(n)


Sorting: O(log n) to O(n) depending on sort algorithm
Result array: O(n) in worst case if all adjacent pairs have same difference
Overall: O(n)

"""
