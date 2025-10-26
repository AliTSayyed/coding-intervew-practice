"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
"""


class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        # initilize length of array to return
        dp = [0 for i in range(n + 1)]

        # the amount of 1s at each number is the same as the amount of 1s
        # in number // 2 + 1 if the number is odd, 0 if even
        # need to write the bits out on paper to see this pattern
        for i in range(1, n + 1):
            dp[i] = dp[i // 2] + (i % 2)
        return dp


"""
# Count Bits - Problem Summary

## 1. Pattern Recognition

**Pattern:** Dynamic Programming (Bottom-Up Tabulation)

**Key Characteristics:**
- Problem asks to compute values for a range (0 to n)
- Current value depends on a previously computed smaller value
- Optimal substructure: answer for `i` can be built from answer for `i // 2`
- Avoids recalculating the same bit counts repeatedly

**Similar Problems:**
- Climbing Stairs (each step depends on previous steps)
- Fibonacci Numbers (build from smaller subproblems)
- Pascal's Triangle (each value built from previous row)
- Any problem where "the answer for n uses the answer for n/2 or n-1"

## 2. High-Level Approach

For each number from 0 to n, calculate the count of 1s in its binary representation by reusing the count from a smaller number (i // 2). The relationship is: the count of 1s in any number equals the count in that number divided by 2, plus 1 if the number is odd (rightmost bit is 1), or plus 0 if even.

## 3. Step-by-Step Logic

1. **Create result array** of size n+1 to store counts for all numbers 0 through n
   - *Why:* Need to store one count for each number in our range

2. **Base case:** Set dp[0] = 0 
   - *Why:* Zero has no 1s in binary (though this happens automatically with initialization)

3. **Build up from 1 to n:** For each number i, calculate dp[i] = dp[i // 2] + (i % 2)
   - *Why:* When you divide a number by 2 (shift right in binary), you remove the rightmost bit. The number of 1s equals whatever the smaller number (i//2) had, plus 1 if we removed a 1-bit (odd number), or plus 0 if we removed a 0-bit (even number)
   - *Why it works sequentially:* Since i // 2 < i, we've always already calculated the value we need

4. **Return the complete array**

## 4. Key Insights & Edge Cases

**What makes this work:**
- Binary representation relationship: Any number's bit count = (that number's half's bit count) + (1 if odd, 0 if even)
- Example: 5 is `101`, and 5//2 = 2 is `10`. We see 5 has the same 1s as 2, plus one more from the rightmost bit

**Implementation Details:**
- Use `i % 2` to check if rightmost bit is 1 (odd) or 0 (even)
- Use `i // 2` for integer division (equivalent to right-shift but more readable)
- Could also use bitwise operators: `i & 1` and `i >> 1`, but modulo/division is clearer

**Edge Cases:**
- n = 0: Returns [0] ✓
- n = 1: Returns [0, 1] ✓
- All cases handled by the formula

## 5. Pseudocode

```
function countBits(n):
    create array dp of size n+1
    
    dp[0] = 0  // base case
    
    for i from 1 to n:
        dp[i] = dp[i // 2] + (i % 2)
    
    return dp
```

## 6. Complexity Analysis

**Time Complexity:** O(n)
- Single loop from 1 to n
- Each iteration does O(1) work (one division, one modulo, one addition, one lookup)

**Space Complexity:** O(n)
- Array of size n+1 to store all results
- Note: This is optimal since we must return an array of size n+1
"""
