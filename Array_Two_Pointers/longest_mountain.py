"""

You may recall that an array arr is a mountain array if and only if:
arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

Example 1:
Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

"""


class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # keep track of mountain length
        ret = 0

        # mountain peak can not be at an edge
        for i in range(1, len(arr) - 1):
            # identify a peak, there can be multiple
            if arr[i - 1] < arr[i] > arr[i + 1]:
                l = r = i

                # check decreasing order to the left of the current peak
                while l > 0 and arr[l] > arr[l - 1]:
                    l -= 1

                # check decreasing order to the right of the current peak
                while r < len(arr) - 1 and arr[r] > arr[r + 1]:
                    r += 1

                # take the max of the current mountian sub array range
                # ensures we get the longest mountain if there are many peaks
                ret = max(ret, (r - l) + 1)

        return ret


"""
High-Level Approach
Use peak detection + expansion from center to find all mountains and track the longest one.
The Strategy
1. Identify Valid Peaks
A peak must have a smaller value on both sides: arr[i-1] < arr[i] > arr[i+1]
Peaks cannot be at the edges (indices 0 or n-1) because mountains need both ascending and descending sections
Loop through indices 1 to n-2 to find all potential peaks
2. Expand from Each Peak
Once a peak is found, expand in both directions to measure the full mountain
Expand left: Move left while values are strictly descending (retracing the upward climb)
Expand right: Move right while values are strictly descending (following the downward slope)
Stop expansion when you can't go further (reaching array bounds or breaking the strict decrease pattern)
3. Calculate Mountain Length
After expanding, you have two pointers: l (leftmost index) and r (rightmost index)
Length = (r - l) + 1 (the +1 includes both endpoints)
Track the maximum length found across all peaks
4. Handle Edge Cases
Return 0 if no valid mountains exist
Arrays with only ascending or only descending values have no mountains
Multiple peaks may exist - only return the longest mountain
Key Implementation Details
Boundary Checking
When expanding left: check l > 0 before accessing arr[l-1] to prevent out of bounds
When expanding right: check r < len(arr) - 1 before accessing arr[r+1] to prevent out of bounds
These checks prevent invalid array accesses, but the pointers themselves can reach the edges
Why This Pattern Works
Peaks are the defining feature of mountains - they guarantee both ascending and descending sections exist
Expanding from peaks naturally measures the full mountain extent
Similar to "expand from center" pattern used in palindrome problems
Complexity
Time: O(n) - each element visited at most twice (once in main loop finding peaks, once during expansion). O(n^2) worst case (situation like [1,2,1,2,1,2,1,2])
Space: O(1) - only using a few pointer variables and the result tracker
Pattern Recognition
This is an expansion from center problem where:
The "center" is the peak
You expand outward to find the full extent
You're looking for a specific pattern (strictly increasing then strictly decreasing)

"""
