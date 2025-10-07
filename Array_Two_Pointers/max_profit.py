"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # left pointer at the start of the array
        # right pointer starts to the right of the left pointer
        l, r = 0, 1

        max_profit = 0
        # start loop until the right pointer exits the array
        while r != len(prices):
            # case where there is a profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            # update the new "lowest" number for calculating profit
            else:
                l = r

            # move r no matter what
            r += 1

        return max_profit


"""
O(N) time
This is a classic example of a greedy algorithm. The greedy algorithm is great for optimization problems, specifically when you need to find the minimum or maximum result. There can be only one solution or no solution, never multiple solutions.  Now, there are other ways to solve optimization problems such as dynamic programming and branch and bound method, but the approaches are different than the greedy method.

The general method of the greedy algorithm is as follows: Algorithm Greedy(a,n) where a is the array and n is number of items in the array
{
	for i = 1 to n do {
		x = Select(a);
		If Feasible(x) then {
			Solution = Solution + x;
}
}
}

Where the Feasible method is some way we are determining that this x value satisfies the constraint

In this problem the algorithm is doing two things simultaneously:
Keep tracking the lowest price seen so far (that's what l represents)
Calculate profit for every potential sell day using that lowest price
Visual Way to Think About It
prices = [7, 1, 5, 3, 6, 4]

Start with l = 7
See 1? That's lower! Update l = 1 (new best buy price)
See 5? Calculate profit: 5 - 1 = 4 ✓
See 3? Calculate profit: 3 - 1 = 2 (not better than 4)
See 6? Calculate profit: 6 - 1 = 5 ✓ (new max!)
See 4? Calculate profit: 4 - 1 = 3 (not better than 5)
Result: Max profit = 5 (buy at 1, sell at 6)
The Beauty of This Approach
By always keeping the minimum buy price, every subsequent number we check automatically gives us the maximum possible profit for that selling day. We don't need to check all pairs - just keep the best buy and check each potential sell!
"""
