"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]
"""


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefixSum = nums[:]
        # convert to a prefix sum
        for i in range(1, len(nums)):
            self.prefixSum[i] += nums[i - 1]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # prefixSum[left - 1] = everything you don't want (indices 0 to left-1)
        # Subtract it from prefixSum[right] to isolate just your range.
        # prefixSum[right] is the sum of all values from index 0 to right

        if left == 0:
            return self.prefixSum[right]
        else:
            return self.prefixSum[right] - self.prefixSum[left - 1]


"""
# Range Sum Query - Immutable - Problem Summary

## 1. Pattern Recognition

**Pattern:** Prefix Sum (Cumulative Sum) Array with Preprocessing

**Key Characteristics:**
- Problem involves **multiple queries** on the same static array
- Queries ask for **range sums** (sum of elements between two indices)
- Array doesn't change between queries (immutable)
- Need to optimize repeated range queries
- Trade-off: preprocessing time/space for faster query time

**Trigger Words:**
- "Multiple queries"
- "Range sum" / "sum between indices"
- "Immutable array" / "array doesn't change"
- Class-based design with initialization

**Similar Problems:**
- Range Sum Query 2D (2D prefix sums)
- Subarray Sum Equals K (uses prefix sums with hashmap)
- Contiguous Array (prefix sum variation)
- Product of Array Except Self (similar preprocessing concept)
- Any problem asking for efficient range queries on static data

## 2. High-Level Approach

Build a prefix sum array during initialization where each index stores the cumulative sum from the start of the array up to that point. Add a dummy 0 at the beginning to handle edge cases. To answer range sum queries, subtract the prefix sum at the left boundary from the prefix sum at the right boundary, giving you the sum of elements in that range in constant time.

## 3. Step-by-Step Logic

1. **Preprocessing in __init__:**
   - Create prefix sum array of size n+1 (one extra for dummy value)
   - *Why:* The extra space avoids edge case handling when left=0
   
2. **Set index 0 to 0 (dummy value)**
   - *Why:* Represents "sum of nothing" - makes the subtraction formula work for all cases without conditionals

3. **Build prefix sums:** For each index i (1 to n), calculate prefix[i] = prefix[i-1] + nums[i-1]
   - *Why:* Each position stores the cumulative sum up to that point in the original array
   - *Why this works:* Current sum = previous sum + next element (efficient one-pass construction)

4. **Answer queries:** Return prefix[right+1] - prefix[left]
   - *Why:* prefix[right+1] contains sum from 0 to right; prefix[left] contains sum from 0 to left-1
   - Subtraction removes everything before index left, leaving only the range [left, right]

## 4. Key Insights & Edge Cases

**What makes this solution work:**
- **Mathematical insight:** sum(left to right) = sum(0 to right) - sum(0 to left-1)
- **Preprocessing trade-off:** Spend O(n) time once to make all future queries O(1)
- **Offset trick:** Adding dummy 0 at index 0 eliminates special case handling

**Implementation Details:**
- Array is shifted by 1: prefix[i] corresponds to sum of first i elements of original array
- Use `prefix[right+1]` not `prefix[right]` due to the shift
- Initialize with `[0] * (len(nums) + 1)` for cleaner, faster code than list comprehension

**Edge Cases:**
- left = 0 (query from start): Works automatically due to dummy 0
- left = right (single element): prefix[right+1] - prefix[right] = nums[right] ✓
- Empty range: Handled by construction
- Full array query (0, n-1): Works naturally with formula

## 5. Pseudocode

```
class NumArray:
    function __init__(nums):
        create prefix array of size len(nums) + 1
        prefix[0] = 0  // dummy value
        
        for i from 1 to len(nums):
            prefix[i] = prefix[i-1] + nums[i-1]
        
        store prefix as instance variable
    
    function sumRange(left, right):
        return prefix[right + 1] - prefix[left]
```

## 6. Complexity Analysis

**Time Complexity:** 
- `__init__`: O(n) - single pass to build prefix sum array
- `sumRange`: O(1) - two array lookups and one subtraction
- Overall: O(n) preprocessing, O(1) per query (optimal for multiple queries)

**Space Complexity:** O(n)
- Prefix sum array of size n+1
- Note: This is the trade-off for constant-time queries. Without preprocessing, space would be O(1) but queries would be O(n)
"""
