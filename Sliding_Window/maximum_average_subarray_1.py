"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
"""


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # calculate the initial window sum and average
        window_sum = sum(nums[:k])
        max_avg = window_sum / k

        # change the value of the window sum to account for the next number
        # and remove the old number (this slides the window)
        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i - k]
            avg = window_sum / k
            max_avg = max(max_avg, avg)

        return max_avg

        # O(n x k) slower version
        # left = 0
        # right = k
        # max_avg = float('-inf')

        # while right <= len(nums):
        #     avg = (sum(nums[left:right]) / k)

        #     max_avg = max(max_avg, avg)

        #     left += 1
        #     right += 1

        # return max_avg


"""
1. Pattern Recognition
Pattern: Sliding Window (Fixed Size)
Key Characteristics:
Looking for optimal value in ALL contiguous subarrays of a fixed size
Need to examine every window of exactly k elements
Calculating an aggregate metric (sum, average, max, etc.) for each window
Similar Problems:
Maximum sum subarray of size k
Minimum sum subarray of size k
Contains duplicate within k distance
Maximum of all subarrays of size k
2. High-Level Approach
Calculate the sum of the first k-element window, then slide the window one position at a time by removing the leftmost element and adding the next element. Track the maximum sum (or average) encountered across all windows.
3. Step-by-Step Logic
Initialize the first window: Calculate the sum of the first k elements


Why: We need a starting point and this establishes our initial window
Set initial maximum: Use the first window's average as the initial max_avg


Why: We need something to compare against as we slide
Slide the window: For each remaining element in the array:


Add the new element entering the window (right side)
Subtract the old element leaving the window (left side)
Why: This maintains the window sum in O(1) time instead of recalculating from scratch
Update maximum: After each slide, compare current average with max_avg


Why: We're looking for the maximum across ALL windows
Return the maximum average


4. Key Insights & Edge Cases
What Makes It Work:
The running sum trick: instead of recalculating sum for each window, we update it incrementally
Only the elements at the boundaries change between consecutive windows
Important Details:
Python 2 vs 3: Use float(k) or float(sum) to ensure float division, not integer division
The window size stays constant at k throughout
Loop from index k to len(nums) since we already processed the first window
Edge Cases:
When k equals the array length (only one window exists)
Negative numbers in the array (doesn't affect the algorithm)
k = 1 (every element is its own window)
5. Pseudocode
function findMaxAverage(nums, k):
    // Initialize first window
    window_sum = sum of first k elements
    max_avg = window_sum / k
    
    // Slide window through rest of array
    for i from k to end of nums:
        // Update window: add new, remove old
        window_sum = window_sum + nums[i] - nums[i-k]
        
        // Calculate new average
        current_avg = window_sum / k
        
        // Update maximum if needed
        max_avg = max(max_avg, current_avg)
    
    return max_avg

6. Complexity Analysis
Time Complexity: O(n)
Initial sum calculation: O(k)
Sliding window loop: O(n - k) iterations, each doing O(1) work
Total: O(k) + O(n - k) = O(n)
Space Complexity: O(1)
Only storing a few variables (window_sum, max_avg, loop counter)
No additional data structures that grow with input size
"""
