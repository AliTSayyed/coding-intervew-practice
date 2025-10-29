"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
"""


class Solution(object):
    def twoSum2(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = 0
        l = len(numbers) - 1

        while numbers[r] + numbers[l] != target:
            if numbers[r] + numbers[l] < target:
                r += 1
            else:
                l -= 1

        return [r + 1, l + 1]


"""
# LeetCode 167: Two Sum II - Input Array Is Sorted

## 1. Pattern Recognition

**Pattern:** Two Pointers (Opposite Ends)

**Key Characteristics:**
- Array is **sorted** (this is the critical hint!)
- Looking for a pair that satisfies a condition (sum equals target)
- Need to find exactly one solution
- Constraint: O(1) space (can't use hash map like regular Two Sum)
- Working with opposites (smallest + largest, then adjust)

**Similar Problems:**
- LeetCode 15: 3Sum
- LeetCode 11: Container With Most Water
- LeetCode 125: Valid Palindrome
- LeetCode 977: Squares of a Sorted Array
- Any problem with sorted array + find pair/triplet

## 2. High-Level Approach

Use two pointers starting at opposite ends of the sorted array. If the sum is too small, move the left pointer right to increase the sum. If the sum is too large, move the right pointer left to decrease the sum. Continue until you find the target sum.

## 3. Step-by-Step Logic

1. **Initialize two pointers: left at start (index 0), right at end (last index)**
   - Why: In a sorted array, smallest value is at the start, largest at the end

2. **Calculate sum of elements at both pointers**
   - Why: Check if we've found our target

3. **If sum < target, move left pointer right (increment)**
   - Why: Array is sorted, so moving left pointer right increases the sum
   - We need a bigger number to reach the target

4. **If sum > target, move right pointer left (decrement)**
   - Why: Moving right pointer left decreases the sum
   - We need a smaller number to reach the target

5. **If sum == target, return the indices (1-indexed)**
   - Why: We found our answer

6. **Repeat until solution found**
   - Why: Problem guarantees exactly one solution exists

## 4. Key Insights & Edge Cases

**Key Insights:**
- **Sorted array is the key:** This is what makes two pointers work efficiently
- **Monotonic adjustment:** Moving left pointer only increases sum, moving right pointer only decreases sum
- **No need to check all pairs:** We eliminate possibilities with each move (O(n) instead of O(n²))
- **Guaranteed solution:** We can use a simple while loop without worrying about no solution case

**Implementation Details:**
- Return 1-indexed positions (add 1 to both indices)
- Your variable naming is backwards (r=0 should be left, l=len-1 should be right), but logic is correct!
- Problem guarantees exactly one solution, so no need for error handling

**Edge Cases:**
- Array with 2 elements: Still works, pointers at opposite ends
- Negative numbers: Still works because array is sorted
- Target is sum of first and last: Found immediately
- Target requires middle elements: Pointers will converge to them

## 5. Pseudocode

```
function twoSum(numbers, target):
    left = 0
    right = length - 1
    
    while true:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  // 1-indexed
        
        if current_sum < target:
            left++  // need bigger sum
        else:
            right--  // need smaller sum
```

## 6. Complexity Analysis

**Time Complexity:** O(n)
- Each pointer moves at most n times
- We visit each element at most once
- Single pass through the array

**Space Complexity:** O(1)
- Only using two pointer variables (left and right)
- No extra data structures (hash map, arrays, etc.)
- Meets the constant space requirement
"""
