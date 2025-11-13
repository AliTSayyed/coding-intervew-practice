"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

"""


class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # if mid < right, the right half is sorted (no pivot there)
            # so minimum must be in left half or IS mid
            if nums[mid] < nums[right]:
                right = mid

            # if mid > right, there's a "break" in the right half
            # so the minimum (pivot point) is in the right half
            elif nums[mid] > nums[right]:
                left = mid + 1

            # if mid == right, we've converged on the minimum
            else:
                return nums[mid]


"""
1. Pattern Recognition
Pattern: Modified Binary Search (Finding Pivot/Breakpoint)
Key Characteristics:
Rotated sorted array (one "break" point where order resets)
Need O(log n) time → binary search
Looking for a specific element (minimum) not a target value
The minimum is at the rotation pivot point
Similar Problems:
LC 154: Find Minimum in Rotated Sorted Array II (with duplicates)
LC 33: Search in Rotated Sorted Array
LC 162: Find Peak Element
Any problem finding breakpoints/pivots in modified sorted arrays
2. High-Level Approach
Use binary search to locate the rotation pivot (minimum element) by comparing mid with the rightmost element. If mid is greater than right, the pivot is in the right half; if mid is less than right, the pivot is in the left half or IS mid. Converge the pointers until they meet at the minimum.
3. Step-by-Step Logic
Initialize pointers: Set left = 0, right = len(nums) - 1


Why: Standard binary search setup
Calculate mid: mid = (left + right) // 2


Why: Check the middle element to decide which half contains the minimum
Compare nums[mid] with nums[right]:


Why: The right boundary tells us if there's a "break" (rotation pivot) in the right half
If nums[mid] < nums[right]:


The right half [mid+1...right] is properly sorted (no break there)
Minimum must be in [left...mid] including mid itself
Set right = mid (NOT mid - 1, because mid could be the answer)
Why: No pivot on the right means it must be on the left or IS mid
If nums[mid] > nums[right]:


There's a break/pivot somewhere in [mid+1...right]
The minimum is in the right half
Set left = mid + 1 (mid can't be minimum since it's larger than right)
Why: The break indicates the rotation point is to the right
If nums[mid] == nums[right]:


Pointers have converged (left == mid == right)
Return nums[mid]
Why: We've found the single element that is the minimum
4. Key Insights & Edge Cases
What Makes This Work:
The minimum element is always where the array "breaks" (larger value followed by smaller value)
Comparing with the RIGHT element (not left) cleanly identifies which half contains the break
Unlike LC 33, we don't need to identify sorted halves - just where the pivot is
Implementation Details:
Use right = mid (NOT mid - 1) when nums[mid] < nums[right] because mid could be the minimum
Use left = mid + 1 when nums[mid] > nums[right] because mid is definitely not the minimum
Can use while left < right with return nums[left] OR while left <= right with explicit return when converged
Edge Cases:
Array not rotated (already sorted) - still works! Mid will always be < right, converges to first element
Single element array - immediately returns
Minimum at first position
Minimum at last position
5. Pseudocode
function findMin(nums):
    left = 0
    right = length - 1
    
    while left <= right:
        mid = (left + right) / 2
        
        if nums[mid] < nums[right]:
            # Right half is sorted, minimum is on left or IS mid
            right = mid
        
        elif nums[mid] > nums[right]:
            # Break is in right half, minimum is there
            left = mid + 1
        
        else:
            # Converged: left == mid == right
            return nums[mid]
    
    # Alternative: use while left < right, then return nums[left]

6. Complexity Analysis
Time Complexity: O(log n)
Binary search halves the search space each iteration
Maximum log₂(n) iterations to converge
Space Complexity: O(1)
Only using constant extra space (left, right, mid pointers)
No recursion or additional data structures

"""
