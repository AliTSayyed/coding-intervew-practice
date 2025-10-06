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
