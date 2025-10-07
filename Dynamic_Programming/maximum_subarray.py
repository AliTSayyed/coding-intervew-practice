"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # initilize the max possible subarray to -inf so only a correct max replaces this
        current_max = float("-inf")

        # this value stores the max total sum up to the current index
        total = 0

        # for each value in the array, calculate if it helps increase the total, or we should
        # start fresh and use that new value as the total
        for i, val in enumerate(nums):
            total += val
            max_sum = max(total, val)

            # start fresh
            if max_sum == val:
                total = val

            # store max total we have seen throughout the array
            current_max = max(current_max, max_sum)

        return current_max


"""
# Maximum Subarray Problem - Study Notes

## 1. Pattern Recognition
* **Pattern:** Dynamic Programming (Kadane's Algorithm) / Greedy
* **Key Characteristics:**
  - Asks for "maximum sum" of a contiguous subarray
  - Need to make local decisions (extend vs. start fresh) at each position
  - Current decision depends on previous state (extend previous subarray or not)
  - Can't sort or rearrange (must maintain subarray order)
  - Optimal substructure: best subarray ending at position i depends on best ending at i-1
* **Similar Problems:**
  - Maximum Product Subarray
  - Best Time to Buy and Sell Stock
  - Longest Turbulent Subarray
  - Maximum Sum Circular Subarray
  - House Robber (similar DP decision-making pattern)

## 2. High-Level Approach
At each position, decide whether to extend the previous subarray by adding the current element, or start a new subarray from the current element. Choose whichever gives a larger sum. Track the maximum sum seen across all positions as you iterate through the array.

## 3. Step-by-Step Logic
1. **Initialize tracking variables:** Set overall maximum to negative infinity and current subarray sum to 0
   - *Why:* Negative infinity ensures any valid subarray replaces it (handles all-negative arrays); current sum tracks the running subarray

2. **At each position, make a local decision:** Compare extending the current subarray (`current_sum + nums[i]`) vs. starting fresh (`nums[i]`)
   - *Why:* If the previous subarray sum is negative and drags you down, it's better to abandon it and start fresh

3. **Choose the better option:** Take the maximum of the two choices
   - *Why:* This represents the best subarray sum that ends at the current position

4. **Update the global maximum:** Compare current position's best with the overall maximum seen so far
   - *Why:* The answer could be any subarray ending at any position, so track the best across all positions

5. **Return the global maximum:** After processing all elements, return the best sum found
   - *Why:* This is the maximum subarray sum in the entire array

## 4. Key Insights & Edge Cases
**What Makes This Work:**
- **Greedy + DP hybrid:** Makes locally optimal decisions (extend or restart) that lead to globally optimal solution
- **Key insight:** If current running sum becomes negative, it can only hurt future sums, so restart
- **No need to track indices:** Only need to track sums, not where subarrays start/end
- This is **Kadane's Algorithm** - a classic linear-time solution

**Important Details:**
- Must initialize `max_overall` to `float('-inf')`, not 0 (to handle all-negative arrays)
- The decision is binary at each step: `max(current_sum + nums[i], nums[i])`
- Space can be optimized to O(1) since only need previous position's value
- When `max(total + val, val) == val`, you're starting fresh

**Edge Cases:**
- All negative numbers → return the largest (least negative) number
- Single element array → return that element
- Array with mix of positive/negative → algorithm handles naturally
- Empty array → not typically in constraints, but would need special handling

## 5. Pseudocode
```
function maxSubArray(nums):
    max_overall = negative infinity
    current_sum = 0
    
    for each value in nums:
        current_sum = current_sum + value
        best_ending_here = max(current_sum, value)
        
        if best_ending_here equals value:
            current_sum = value  // starting fresh
        
        max_overall = max(max_overall, best_ending_here)
    
    return max_overall
```

**Alternative (more standard) formulation:**
```
function maxSubArray(nums):
    max_overall = negative infinity
    current_sum = 0
    
    for each value in nums:
        current_sum = max(current_sum + value, value)
        max_overall = max(max_overall, current_sum)
    
    return max_overall
```

## 6. Complexity Analysis
* **Time Complexity:** O(n)
  - Single pass through the array
  - Each element processed exactly once with O(1) operations

* **Space Complexity:** O(1)
  - Only using constant extra space (two variables)
  - No additional data structures needed
  - Space-optimized DP (doesn't store entire dp array)
"""
