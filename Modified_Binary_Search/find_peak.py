"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
"""


class Solution:
    def findPeakElement(self, nums) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid < mid+1, we're going uphill
            # A peak MUST exist to the right (either mid+1 or beyond)
            # So eliminate the left half including mid
            if nums[mid] < nums[mid + 1]:
                left = mid + 1

            # If mid > mid+1, we're going downhill
            # Mid could BE the peak, or a peak exists to the left
            # So eliminate the right half BUT keep mid as a candidate
            else:
                right = mid

        return left


"""
1. Pattern Recognition
Pattern: Modified Binary Search (Peak Finding)
Key Characteristics:
Need O(log n) time → binary search
Looking for ANY element satisfying a condition (not a specific target)
Can make a binary decision based on comparing neighbors
Guaranteed that a solution exists (problem states peaks always exist)
Similar Problems:
LC 852: Peak Index in a Mountain Array
LC 1095: Find in Mountain Array
LC 153: Find Minimum in Rotated Sorted Array (finding extrema)
Any problem finding local extrema or breakpoints
2. High-Level Approach
Use binary search by comparing mid with mid+1 to determine if you're on an upward or downward slope. If going uphill (mid < mid+1), a peak must exist to the right, so search right. If going downhill (mid > mid+1), mid could be the peak or a peak exists to the left, so search left while keeping mid as a candidate.
3. Step-by-Step Logic
Initialize pointers: Set left = 0, right = len(nums) - 1


Why: Standard binary search setup, peak must be in array
Calculate mid and compare with mid+1:


Why: Checking the slope direction tells us which way to move toward a peak
If nums[mid] < nums[mid+1] (uphill):


Set left = mid + 1
Why: Going uphill means there MUST be a peak ahead (either mid+1 is peak, or slope continues to one). We can eliminate everything at mid and to the left.
Else nums[mid] > nums[mid+1] (downhill):


Set right = mid (NOT mid - 1)
Why: Mid is greater than its right neighbor (one peak condition satisfied). Mid could BE the peak, or there's a peak to the left. Must keep mid as a candidate.
Continue until left == right:


Why: When pointers converge, we've found a peak
Return left:


Why: Left points to an element that is a local maximum
4. Key Insights & Edge Cases
What Makes This Work:
The algorithm always moves toward "higher ground"
We don't need to find ALL peaks, just ANY peak
By following the upward slope, we're guaranteed to reach a peak
Elements outside array boundaries are treated as -∞ (given by problem), so edge elements can be peaks
Implementation Details:
Use right = mid (NOT mid - 1) in the downhill case because mid might be the peak
Use left = mid + 1 in the uphill case because mid cannot be the peak (something higher exists to its right)
Only need to compare with right neighbor (mid+1), not left neighbor
Use while left < right pattern for clean convergence
Edge Cases:
Single element array - immediately returns (it's a peak by definition)
Strictly increasing array - converges to last element
Strictly decreasing array - converges to first element
Multiple peaks exist - returns any one (algorithm doesn't need to find all)
Peak at array boundaries - handled correctly due to problem's assumption about out-of-bounds elements
5. Pseudocode
function findPeakElement(nums):
    left = 0
    right = length - 1
    
    while left < right:
        mid = (left + right) / 2
        
        if nums[mid] < nums[mid + 1]:
            # Uphill - peak must be to the right
            left = mid + 1
        
        else:
            # Downhill - mid could be peak, or peak is to left
            right = mid
    
    return left  # Converged on a peak

6. Complexity Analysis
Time Complexity: O(log n)
Binary search halves the search space each iteration
Maximum log₂(n) iterations to converge on a peak
Space Complexity: O(1)
Only using constant extra space (left, right, mid pointers)
No recursion or additional data structures

"""
