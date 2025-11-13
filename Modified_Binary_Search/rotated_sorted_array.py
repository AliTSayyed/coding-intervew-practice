"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""


class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums) - 1

        # key is that if one half is not sorted then the other half is!
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid

            # check if this is the sorted half
            elif nums[left] <= nums[mid]:
                # if this half is sorted, then check if target is in the half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # if target is not in this half, we remove this half
                else:
                    left = mid + 1

            # same as above but checking the other half
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


"""
1. Pattern Recognition
Pattern: Modified Binary Search
Key Characteristics:
Sorted array with a twist (rotated at unknown pivot)
Need O(log n) time → binary search
At least one half will always be properly sorted after any split
Similar Problems:
LC 153: Find Minimum in Rotated Sorted Array
LC 81: Search in Rotated Sorted Array II (with duplicates)
LC 162: Find Peak Element
Any problem requiring binary search on modified sorted arrays
2. High-Level Approach
Use binary search, but at each step identify which half (left or right of mid) is properly sorted. Check if the target falls within the sorted half's range. If yes, search that half; if no, eliminate it and search the other half.
3. Step-by-Step Logic
Initialize pointers: Set left = 0, right = len(nums) - 1


Why: Standard binary search setup
Find mid and check if it's the target


Why: Base case - might get lucky immediately
Determine which half is sorted: Compare nums[left] with nums[mid]


If nums[left] <= nums[mid]: left half is sorted
Otherwise: right half is sorted
Why: The rotation pivot can only exist in ONE half, so the other must be properly sorted
Check if target is in the sorted half's range:


For sorted left half: is nums[left] <= target < nums[mid]?
For sorted right half: is nums[mid] < target <= nums[right]?
Why: We can apply normal sorted array logic to the sorted half
Update search bounds:


If target is in sorted half: search that half
If target is NOT in sorted half: eliminate it, search the other half
Why: If target isn't in the sorted half, it MUST be in the other half (or doesn't exist)
Repeat until found or left > right


4. Key Insights & Edge Cases
What Makes This Work:
Exactly one half is always properly sorted after any split
You don't need to find the pivot - just identify the sorted half
Standard binary search logic applies to the sorted half
Implementation Details:
Use < nums[mid] and > nums[mid] in range checks (exclude mid since already checked)
Use <= when comparing nums[left] to nums[mid] to handle when left half has only 1-2 elements
Edge Cases:
Array not rotated at all (entire array sorted) - still works!
Target doesn't exist - returns -1
Single element array
Target at boundaries (first or last element)
5. Pseudocode
function search(nums, target):
    left = 0
    right = length - 1
    
    while left <= right:
        mid = (left + right) / 2
        
        if nums[mid] == target:
            return mid
        
        if left half is sorted (nums[left] <= nums[mid]):
            if target is in sorted left range:
                search left half (right = mid - 1)
            else:
                search right half (left = mid + 1)
        
        else (right half is sorted):
            if target is in sorted right range:
                search right half (left = mid + 1)
            else:
                search left half (right = mid - 1)
    
    return -1 (not found)

6. Complexity Analysis
Time Complexity: O(log n)
Binary search cuts search space in half each iteration
Maximum log₂(n) iterations
Space Complexity: O(1)
Only using constant extra space (left, right, mid pointers)
No recursion stack or additional data structures

"""
