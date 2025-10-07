"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # initlize coin cahce arr
        # the index was storing how many coins it would take to calculate it
        # worst case is that each coin is 1, so initlilize them to all take the max amount of coins
        cache = [(amount + 1) for i in range(amount + 1)]
        # we know 0 value can have 0 coins
        cache[0] = 0

        # loop through index and calculate how many coins would
        # be used to calculate the index value
        # take the min possible coins
        # use previous index values instead of recalculating the same values over agian
        for i in range(1, amount + 1):
            for c in coins:
                # ex: index 1 - coin of value 1 >= 0
                if (i - c) >= 0:
                    # replace the value at the index with how many coins were needed to calculate it
                    min_coins_used = min(cache[i], cache[i - c] + 1)
                    cache[i] = min_coins_used

        # if it was possible to calculate return, else give -1
        if cache[amount] != amount + 1:
            return cache[amount]
        else:
            return -1


"""
1. Pattern Recognition
Pattern: Dynamic Programming (Bottom-Up/Tabulation)
Key Characteristics:
Asks for optimization (minimum/maximum)
Problem has overlapping subproblems (same amounts calculated repeatedly)
Has optimal substructure (optimal solution built from optimal solutions to subproblems)
Unlimited use of resources (infinite coins)
Similar Problems:
Climbing Stairs
House Robber
Longest Increasing Subsequence
Unbounded Knapsack
Minimum Path Sum
2. High-Level Approach
Build up solutions from smallest amounts to target amount, storing the minimum coins needed for each amount. For each amount, try using each coin denomination and keep track of which choice gives the fewest total coins. Use previously computed results to avoid recalculation.
3. Step-by-Step Logic
Create DP array: Index i represents "minimum coins needed to make amount i"


Why: We need to store subproblem solutions to reuse them
Initialize base case: dp[0] = 0 (zero coins needed for zero amount)


Why: This is our foundation that all other solutions build upon
Initialize impossible marker: Set all other values to amount + 1


Why: Worst case is all 1-value coins = exactly amount coins, so amount + 1 means "not yet found/impossible", could use inf but why use such a large number when we don't need to
Build up from 1 to target: For each amount i, try each coin


Why: Must solve smaller subproblems before larger ones (can't calculate dp[7] without knowing dp[6], dp[5], etc.)
For each valid coin: If coin ≤ i, calculate dp[i - coin] + 1 and take minimum with current dp[i]


Why: We're asking "if I use this coin, what's the total?" then keeping the best option
Return result: If dp[amount] still equals amount + 1, return -1; otherwise return dp[amount]


Why: If value unchanged, no valid combination exists
4. Key Insights & Edge Cases
What Makes This Work:
Avoids exponential recalculation by storing results
Each subproblem (amount) is solved exactly once
Trying all coins ensures we find the true minimum
Important Details:
Must check i - coin >= 0 before accessing array (avoid negative indices)
Initialize to amount + 1 not infinity (helps with comparison logic)
Array size must be amount + 1 to include index for target amount
Edge Cases:
amount = 0 → return 0 immediately
No valid combination exists → return -1
Single coin that equals amount → return 1
Coins larger than amount → skip those coins
5. Pseudocode
function coinChange(coins, amount):
    create dp array of size (amount + 1)
    initialize dp[0] = 0
    initialize dp[1..amount] = amount + 1
    
    for i from 1 to amount:
        for each coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    if dp[amount] == amount + 1:
        return -1
    else:
        return dp[amount]

6. Complexity Analysis
Time Complexity: O(amount × coins)


Outer loop runs amount times
Inner loop runs len(coins) times for each amount
Each iteration does O(1) work
Space Complexity: O(amount)


DP array stores one value for each amount from 0 to target
No recursion stack (iterative approach)

"""
