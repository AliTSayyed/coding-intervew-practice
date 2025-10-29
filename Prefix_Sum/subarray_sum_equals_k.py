"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # brute force

        # ps = [0 for i in range(len(nums)+1)]
        # total = 0
        # for i in range(1, len(ps)):
        #     total += nums[i-1]
        #     ps[i] = total

        # count = 0

        # for i in range(len(ps)-1, 0, -1):
        #     j = i - 1
        #     while j >= 0:
        #         if ps[i] - ps[j] == k:
        #             count += 1
        #         j -= 1

        # better way like in two sum, check if the k-i value exists in the set
        # if it does then increment count
        # but instead of using a set, use a hashmap to keep track of frequency
        # this is because the same prefix sum can occur multiple times at different indices
        # each occurrence represents a different subarray that sums to k
        # if we only use a set, we'd only count it once and miss the other valid subarrays
        # with a hashmap, we can increment count by the frequency of that prefix sum
        # giving us the correct total number of subarrays
        # prefix_sum -> count, initialize with 0:1
        ps = {0: 1}
        total = 0
        count = 0

        for num in nums:
            total += num

            # Check if (total - k) exists
            if total - k in ps:
                count += ps[total - k]

            # Add current prefix sum to map
            ps[total] = ps.get(total, 0) + 1

        return count


"""
# LeetCode 560: Subarray Sum Equals K

## 1. Pattern Recognition

**Pattern:** Prefix Sum + Hash Map (Complement Pattern)

**Key Characteristics:**
- Need to find contiguous subarrays with a specific sum
- Can't sort or rearrange the array (must preserve order)
- Need to count occurrences, not just find one solution
- Similar to "two sum" but for subarrays instead of pairs

**Similar Problems:**
- LeetCode 525: Contiguous Array (equal 0s and 1s)
- LeetCode 1: Two Sum
- LeetCode 523: Continuous Subarray Sum
- LeetCode 930: Binary Subarrays With Sum

## 2. High-Level Approach

Track running prefix sums as you iterate through the array. For each position, check if there's a previous prefix sum that, when subtracted from the current prefix sum, equals k. Use a hash map to store the frequency of each prefix sum encountered, because multiple occurrences of the same prefix sum represent multiple valid subarrays.

## 3. Step-by-Step Logic

1. **Initialize hash map with {0: 1}**
   - Why: Handles subarrays that start from index 0 (when prefix_sum itself equals k)

2. **Iterate through array, maintaining running sum (prefix sum)**
   - Why: Prefix sum at index i = sum of all elements from 0 to i

3. **For each position, check if (current_prefix_sum - k) exists in hash map**
   - Why: If prefix_sum[i] - prefix_sum[j] = k, then subarray from j+1 to i sums to k
   - Rearranging: prefix_sum[j] = prefix_sum[i] - k

4. **Add the frequency of (current_prefix_sum - k) to count**
   - Why: Each occurrence represents a different starting point for a valid subarray ending at current position

5. **Update hash map with current prefix sum frequency**
   - Why: This prefix sum might be the complement for future positions

## 4. Key Insights & Edge Cases

**Key Insights:**
- The same prefix sum can occur multiple times, and each occurrence represents a different valid subarray
- Must use hash map (not set) to track frequencies, otherwise you undercount
- The difference between two prefix sums gives you the subarray sum between those positions

**Implementation Details:**
- Initialize with {0: 1} to handle edge case where prefix_sum itself equals k
- Increment frequency in hash map using `map.get(key, 0) + 1`
- Add current sum to map AFTER checking for complement (not before)

**Edge Cases:**
- Empty array: return 0
- Single element equals k: handled by {0: 1} initialization
- Multiple subarrays ending at same position: handled by frequency counting
- Negative numbers: solution still works (prefix sums can decrease)

## 5. Pseudocode

```
function subarraySum(nums, k):
    hash_map = {0: 1}  // prefix_sum -> frequency
    running_sum = 0
    count = 0
    
    for each num in nums:
        running_sum += num
        
        complement = running_sum - k
        if complement exists in hash_map:
            count += hash_map[complement]
        
        increment hash_map[running_sum] by 1
    
    return count
```

## 6. Complexity Analysis

**Time Complexity:** O(n)
- Single pass through the array
- Hash map operations (lookup, insert) are O(1) average case

**Space Complexity:** O(n)
- Hash map can store up to n different prefix sums in worst case
- Example: [1, 2, 3, 4, 5] creates unique prefix sums [0, 1, 3, 6, 10, 15]
"""
