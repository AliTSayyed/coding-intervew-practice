"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing_numbers = []
        set_nums = set(nums)
        for number in range(1, len(nums) + 1):
            if number not in set_nums:
                missing_numbers.append(number)
            else:
                continue
        return missing_numbers


"""
Take the set of the list of numbers. This will remove duplicates. Loop over the range(1, len(nums) + 1). We do a +1 because range excludes last number.
If the value in the range is not in our set, append it to our return list and return at the end. O(N)
"""
