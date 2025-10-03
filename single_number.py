"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]

Output: 1
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0

        # loop through and use the XOR operator on each value
        # all same values will cancel, leaving the sole value as the result
        for num in nums:
            xor ^= num
        
        return xor
