"""
Problem:
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # store the seen values
        seen = set()

        # loop through array, store the allowed "window" in the set length
        for i, num in enumerate(nums):
            # duplicate case
            if num in seen:
                return True

            seen.add(num)

            # remove the first item input in the set (keeps the window valid)
            if len(seen) > k:
                seen.remove(nums[i - k])

        return False  # no duplicates found in the allowed window


"""
High-Level Approach
This is a sliding window question. We can tell from  abs(i - j) <= k, that the range of the sub array we are checking must be of size k or less. Hence we “slide” the “window” to find new combinations. 
Use a sliding window with a hash set to track values within the allowed distance range.
The Strategy
1. Maintain a Sliding Window
Use a set to store values within the current valid window
The window size is at most k elements
As you move through the array, the window slides along, maintaining only the last k elements
2. Check for Duplicates
For each element, check if it already exists in the set
If yes: found a duplicate within distance k, return true immediately
If no: add the current element to the set
3. Keep Window Size Valid
If the set size exceeds k, remove the oldest element (the element that's now too far away)
Remove nums[i-k] when the window becomes too large
This ensures we only check duplicates within the allowed distance
4. No Duplicates Found
If we finish the loop without finding duplicates, return false
Key Insights
Why This Works
The set always contains at most k elements representing the current window
Any duplicate found in the set is guaranteed to be within distance k
By removing elements that fall outside the window, we maintain the distance constraint
The Sliding Window Pattern
Window content: Last k elements seen
Window slides: Remove leftmost element when exceeding size k
Check condition: Does current element exist in window?
Why Use a Set
O(1) lookup to check if value exists
O(1) addition and removal of elements
Perfect for tracking "have we seen this value recently?"
Complexity
Time: O(n) - single pass through array with O(1) set operations
Space: O(min(n, k)) - set stores at most k elements (or n if k is larger than array size)
Pattern Recognition
This is a sliding window + hash set problem where:
You need to track elements within a specific range
You need fast lookups to check for duplicates
The window moves through the array, maintaining a fixed maximum size
Common in problems involving "nearby" or "within distance k" constraints

"""
