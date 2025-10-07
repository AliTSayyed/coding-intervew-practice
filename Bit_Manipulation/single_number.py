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


"""
1. Pattern Recognition
Pattern: Bit Manipulation (XOR)
Key Characteristics:
Elements appear in pairs except one unique element
Constant space requirement (O(1))
Need to "cancel out" duplicates
Linear time requirement
Similar Problems:
Single Number II (elements appear 3 times)
Single Number III (two unique elements)
Missing Number
Find the Duplicate Number
2. High-Level Approach
Use the XOR bitwise operator on all elements in the array. XOR has the special property that a ^ a = 0 (any number XORed with itself equals 0) and a ^ 0 = a (any number XORed with 0 equals itself). Since all duplicates cancel out to 0, only the single unique number remains.
3. Step-by-Step Logic
Initialize result variable to 0 (XOR identity value)
Iterate through each number in the array
XOR the current number with the result variable
Return the final result after all XORs complete
Why it works:
All duplicate pairs XOR to 0: 2 ^ 2 = 0
XOR is commutative and associative: order doesn't matter
0 ^ single_number = single_number
Example: 2 ^ 2 ^ 1 → 0 ^ 1 → 1
4. Key Insights & Edge Cases
Key Insight: XOR's self-canceling property (a ^ a = 0) makes it perfect for finding unique elements among pairs
Why constant space? Only one variable needed regardless of array size
XOR Properties to remember:
a ^ a = 0 (pairs cancel)
a ^ 0 = a (identity)
Commutative: a ^ b = b ^ a
Associative: (a ^ b) ^ c = a ^ (b ^ c)
Edge Cases:
Single element array → returns that element
Large numbers → XOR works on any integer size
Negative numbers → XOR still works correctly
5. Pseudocode
function singleNumber(nums):
    result = 0
    
    for each num in nums:
        result = result XOR num
    
    return result

6. Complexity Analysis
Time Complexity: O(n)
Single pass through the array
XOR operation is O(1)
Space Complexity: O(1)
Only one variable used (result)
No additional data structures that scale with input size
Meets the constant space requirement

"""
