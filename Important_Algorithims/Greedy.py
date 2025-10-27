"""
Greedy algorithims are not used for efficiency (because typically they are not looking at every possible outcome)
The purpose is to find the best outcome at each stage.
When a problem is too complex, go Greedy.
"""


# example is Kadane Algorithim
# At each position in the array, Kadane's algorithm makes a greedy decision:
# Either extend the current subarray by including the current element
# Or start a new subarray from the current element
def max_sub_array(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum
