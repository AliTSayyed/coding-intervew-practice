"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # initialize var
        l = 0
        min_len = float("inf")
        total = 0

        # move right pointer and store total of what is in the sub array
        for r in range(len(nums)):
            total += nums[r]
            # move the left pointer up to find a shorter array
            while total >= target:
                min_len = min(min_len, (r - l + 1))
                # before moving pointer take away from the total
                total -= nums[l]
                l += 1

        if min_len == float("inf"):
            return 0
        else:
            return min_len


"""
1. Pattern Recognition
Pattern: Sliding Window (Two Pointers - variable size window)
Key Characteristics:
Contiguous subarray problem
Finding minimum/maximum length with a sum/product condition
All positive integers (allows greedy shrinking - removing elements always decreases sum)
Optimization problem (min/max)
Similar Problems:
Longest Substring Without Repeating Characters
Maximum Sum Subarray of Size K
Fruit Into Baskets
Longest Subarray with Sum ≤ K
2. High-Level Approach
Use two pointers to maintain a sliding window. Expand the window by moving right to include elements until sum meets the target. Once valid, contract from the left while maintaining validity to find the shortest possible subarray. Track the minimum length seen across all valid windows.
3. Step-by-Step Logic
Initialize: Start with both pointers at beginning, sum at 0, minLength at infinity
Expand Phase: Move right pointer, add current element to running sum
Contract Phase: While sum ≥ target (valid window):
Record current window length as potential answer
Remove leftmost element from sum
Move left pointer forward
WHY: Try to find a shorter valid subarray by removing unnecessary elements
Repeat: Continue expanding right until array end is reached
Return: minLength if found, otherwise 0
Why this works: Every element is visited exactly once by each pointer. The greedy contraction is safe because all numbers are positive - removing any element can only decrease the sum.
4. Key Insights & Edge Cases
Critical Insight: Use WHILE loop for contraction, not IF - you may be able to shrink multiple times per expansion
Greedy works here: Since all numbers are positive, if removing the leftmost element still keeps sum ≥ target, that's always better (shorter length)
Window length formula: right - left + 1 (not right - left)
Edge Cases:
No valid subarray exists → return 0
Single element meets target → return 1
Entire array needed → return array length
Empty array → return 0
5. Pseudocode
Initialize:
    left = 0
    minLength = infinity
    currentSum = 0

For right from 0 to end of array:
    Add nums[right] to currentSum
    
    While currentSum >= target:
        Update minLength = min(minLength, right - left + 1)
        Subtract nums[left] from currentSum
        Increment left
        
Return minLength if minLength != infinity, else return 0

6. Complexity Analysis
Time Complexity: O(n)
Each element is added once (right pointer) and removed at most once (left pointer)
Despite nested loops, each element is processed exactly twice in total
Both pointers only move forward, never backward
Space Complexity: O(1)
Only using a few variables regardless of input size
No additional data structures needed

"""
