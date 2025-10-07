"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # store how many ways it takes to reach each stair level from 0 - n inclusive
        dp = [0 for i in range(n + 1)]

        # base case, we know its only 1 way to reach step 0 and 1 way to reach step 1
        # 0 steps has 1 way else the fibonacci sequence would not work
        dp[0] = 1
        dp[1] = 1

        # run fibonacci sequence
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # return the number of ways it takes for the number we are interested in
        return dp[n]


"""
## 1. Pattern Recognition
* **Pattern:** Dynamic Programming (Bottom-Up) / Fibonacci Sequence
* **Key Characteristics:**
  - Asks for "count of ways" (not optimization like min/max)
  - Current state depends on exactly 2 previous states
  - Has overlapping subproblems (ways to reach step i depends on i-1 and i-2)
  - Has optimal substructure (solution built from smaller subproblems)
  - Can only move forward by fixed amounts (1 or 2 steps)
* **Similar Problems:**
  - Fibonacci Number
  - Min Cost Climbing Stairs
  - House Robber
  - Decode Ways
  - Jump Game variations

## 2. High-Level Approach
To reach any step, you must have come from either one step below (taking a 1-step) or two steps below (taking a 2-step). Therefore, the total ways to reach step i equals the sum of ways to reach step i-1 plus ways to reach step i-2. Build up from the base cases using this recurrence relation.

## 3. Step-by-Step Logic
1. **Identify the recurrence:** To reach step i, you either came from step i-1 or step i-2
   - *Why:* You can only take 1 or 2 steps at a time, so these are the only two possibilities

2. **Set up DP array:** Index i represents "number of ways to reach step i"
   - *Why:* We need to store subproblem solutions to build larger solutions

3. **Initialize base cases:** `dp[0] = 1` and `dp[1] = 1`
   - *Why:* One way to reach step 0 (stay there), one way to reach step 1 (take one step)
   - Note: `dp[0] = 1` is mathematical convenience to make the formula work correctly

4. **Apply recurrence relation:** For each step from 2 to n, calculate `dp[i] = dp[i-1] + dp[i-2]`
   - *Why:* All paths through i-1 (then +1 step) plus all paths through i-2 (then +2 steps) give total paths to i

5. **Return result:** `dp[n]` contains the answer
   - *Why:* We built up all values from 0 to n, so dp[n] has the final count

## 4. Key Insights & Edge Cases
**What Makes This Work:**
- The problem is exactly the Fibonacci sequence in disguise
- Each step combines results from exactly two previous steps
- No need to track actual paths, just count them

**Important Details:**
- Array size must be `n+1` to include index n
- `dp[0] = 1` is crucial for the math to work (represents "empty path")
- Loop must start at index 2 (base cases are 0 and 1)
- This is a "counting paths" DP, not "optimization" DP

**Edge Cases:**
- `n = 0` → return 1 (already at destination)
- `n = 1` → return 1 (only one way: take 1 step)
- `n = 2` → return 2 (two ways: [1,1] or [2])

## 5. Pseudocode
```
function climbStairs(n):
    create dp array of size (n + 1)
    initialize dp[0] = 1
    initialize dp[1] = 1
    
    for i from 2 to n:
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

## 6. Complexity Analysis
* **Time Complexity:** O(n)
  - Single loop from 2 to n
  - Each iteration does O(1) work (simple addition)

* **Space Complexity:** O(n)
  - DP array stores n+1 values
  - Note: Can be optimized to O(1) by only keeping track of last two values (since we only need i-1 and i-2)
"""
