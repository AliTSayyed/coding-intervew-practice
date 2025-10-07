"""
Problem:
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100]

"""


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # stores the correct squared order of nums
        answer = []

        l_ptr, r_ptr = 0, len(nums) - 1

        # compare the values at both ends and insert the greater into the array
        # use equal to so we can add the last value into the array
        while l_ptr <= r_ptr:
            l_value, r_value = abs(nums[l_ptr]), abs(nums[r_ptr])

            # since original array is sorted, compare if the first value's absolute
            # is greater than the final value in the original array
            if l_value > r_value:
                answer.append(l_value * l_value)
                l_ptr += 1
            else:
                answer.append(r_value * r_value)
                r_ptr -= 1

        # convert back to list
        return answer[::-1]  # reverse to get ascending order


"""
There are 3 types of solutions we can use. The most basic which is O(nlogn) time, and the other two using pointers with O(N) time.

Basic one is simple, make a new list with all values squared and then sort the new list. Sorting takes log n time so that's what makes the complexity slow.
The primary issue here are the negative signs. If there were no negatives then a sorting method would not be needed. The next two approaches use this logic.

The second way of doing it is essentially checking if negatives exist explicitly. If there are no negatives, return the squared array list. If there are negatives, split the list into two.
The first list is the positive numbers and the second list is all negatives. 
Create a new list which is the reverse of the negative list and multiply each number by -1.
Then create a merge where you select the smaller of the two numbers in each array and add it to one array.
Then return the square of the list.

The third way of doing it is by implicitly addressing negatives by using the Absolute value.
Create a storage array and make a left and right pointer. Start the right pointer at the end of the array and the left pointer at the beginning of the array.
Compare the absolute values at the pointers and insert the square of the higher number to the array. 
After each insert, move the respective pointer either down or up.
Since we built the array in descending order, return the reverse of the result.

"""
