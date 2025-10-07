"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = {}
        for i, num in enumerate(nums):
            # consider negatives in out list?
            current = nums[i]
            looking_for = target - current
            pair = values.get(looking_for)
            if pair is not None:
                return [i, pair]
            else:
                values.update({current: i})


"""
subtract the target value from out current value in the array. Then check if that value exists in our hashmap. 
If that value does not exist in the hashmap then we add our current value and its index into the hashmap. 
Since there can only be one exact solution we know that the target value - our current value = value we need. 
We store values in the hashmap after we check if there is a value that exists in our hashmap to avoid using the same value.
"""
