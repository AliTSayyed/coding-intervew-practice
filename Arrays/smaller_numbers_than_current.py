"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
"""


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hash_map = {}
        sorted_nums = sorted(nums)
        for i, num in enumerate(sorted_nums):
            if hash_map.get(num) is None:
                hash_map[num] = i

        ret = []
        for num in nums:
            ret.append(hash_map.get(num))
        return ret


"""
Sort the array. When the array is sorted, the index at which a number appears (first non duplicates), is how many numbers it is greater than.
Loop over the sorted array and add the value and index into a hashmap, 
if the value already exists in the hashmap just skip since we need the first non duplicate index value 
(has the correct amount of  greater than other numbers as the index). 
Then loop through the num array and append to a list the indexes (stored as values in the hashmap) 
for the numbers you come across in the array. O(nlogn) since sorting in logn and we iterate through each value in the list hence nlogn.

"""
