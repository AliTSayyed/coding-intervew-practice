"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # populate with unique index,right,left === 0
        triplets = []
        # sort the incoming array, this will ensure pointers that go up use increasing values
        # and poitners that go down will use decreasing values
        nums.sort()
        for index, value in enumerate(nums):
            # skip duplicate values since they wont help reach the answer or are already included
            if (index > 0) and (value == nums[index - 1]):
                continue
            # not possible to get a sum of 0 if all point to positive values
            if value > 0:
                break
            left = index + 1
            right = len(nums) - 1
            # use two pointers to check all possible combonations with current index value
            while left < right:
                current_sum = value + nums[left] + nums[right]
                # decrease right pointer will give a lower sum value since array is sorted
                if current_sum > 0:
                    right -= 1
                # increase left pointer will give a higher sum value since array is sorted
                elif current_sum < 0:
                    left += 1
                # sum == 0, add unique triplet, move pointers to evaluate next triplet
                else:
                    triplets.append([value, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # avoid duplicates if new pointers refer to the same value
                    while (left < right) and (nums[left] == nums[left - 1]):
                        left += 1
                    while (left < right) and (nums[right] == nums[right + 1]):
                        right -= 1
        return triplets


"""
High-Level Approach
Sort the array first, then use a fixed pointer + two-pointer technique to find all unique triplets that sum to zero.
The Strategy
1. Sort the Array
Makes it possible to use two pointers efficiently
Helps identify and skip duplicates easily
2. Fix One Element, Search for Two Others
Loop through each element as the "first" element of the triplet
For each fixed element, use two pointers to find the other two numbers
3. Two-Pointer Search
Left pointer: starts right after the fixed element
Right pointer: starts at the end of array
Move pointers based on the sum:
Sum too large? Move right pointer left (decrease sum)
Sum too small? Move left pointer right (increase sum)
Sum equals zero? Found a triplet!
4. Avoid Duplicates in 3 Places
Outer loop: Skip if current element equals previous element
After finding triplet: Skip duplicate values for left pointer
After finding triplet: Skip duplicate values for right pointer
5. Optimization
If the fixed element is positive, stop searching (can't sum to zero with all positive numbers)
Why It Works
Sorting enables efficient two-pointer traversal
Moving both pointers after finding a triplet explores all possibilities
Skipping duplicates ensures we only add unique triplets
Complexity
Time: O(n²) - one loop containing a two-pointer scan
Space: O(n) - triplets list stored
"""
