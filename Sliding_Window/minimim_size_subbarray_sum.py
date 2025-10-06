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
        min_len = float('inf')
        total = 0

        # move right pointer and store total of what is in the sub array
        for r in range(len(nums)):
            total += nums[r]
            # move the left pointer up to find a shorter array
            while total >= target:
                min_len = min(min_len, (r-l+1))
                # before moving pointer take away from the total
                total -= nums[l]
                l += 1
        
        if min_len == float('inf'):
            return 0
        else:
            return min_len
