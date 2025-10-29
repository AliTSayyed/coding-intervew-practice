"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
"""


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # convert all 0s to -1
        # proceed to do a prefix sum
        # insert the sum into a map with its responding index
        # each time c heck that if the hashmap has the same sum then calculate the difference between the indecies.
        # the same sum means that at that between t
        # Initilizae with 0: -1 to hadnle sum becoming 0
        # We've seen a sum of 0 before we even started (at position -1).
        seenSums = {0: -1}
        sum = 0
        max_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                sum -= 1
            else:
                sum += 1
            if sum in seenSums:
                max_length = max(max_length, (i - seenSums[sum]))
            else:
                seenSums[sum] = i

        return max_length


"""
## Summary of the Solution

**Problem:** Find the maximum length of a contiguous subarray with equal number of 0s and 1s.

**Key Insight:** Transform 0s to -1s. If two positions have the same cumulative sum, the subarray between them has sum = 0, meaning equal 0s and 1s.

**Algorithm:**

1. **Initialize:**
   - `max_length = 0`
   - `cumulative_sum = 0`
   - `hash_map = {0: -1}` (to handle subarrays starting from index 0)

2. **Iterate through the array:**
   - For each element:
     - Add `+1` if it's a 1, or `-1` if it's a 0 to `cumulative_sum`
     - **If `cumulative_sum` exists in hash_map:**
       - Calculate length = `current_index - hash_map[cumulative_sum]`
       - Update `max_length` if this length is larger
     - **If `cumulative_sum` NOT in hash_map:**
       - Store it: `hash_map[cumulative_sum] = current_index`

3. **Return `max_length`**

**Time Complexity:** O(n) - single pass through array  
**Space Complexity:** O(n) - hash map storage

**Why it works:** Same cumulative sum at two positions means everything between them canceled out (equal +1s and -1s), which corresponds to equal 0s and 1s in the original array.
"""
