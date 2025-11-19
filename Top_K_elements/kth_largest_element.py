"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?
"""

import heapq


# with sorting version
class Solution:
    def findKthLargestWithSort(self, nums, k: int) -> int:
        if not nums:
            return 0

        nums.sort()

        return nums[len(nums) - k]

    # without sorting but using a max heap

    def findKthLargestWithHeap(self, nums, k: int) -> int:
        if not nums:
            return 0

        for i in range(len(nums)):
            nums[i] = -1 * nums[i]

        heapq.heapify(nums)

        for i in range(k - 1):
            heapq.heappop(nums)

        return heapq.heappop(nums) * -1


"""
1. Pattern Recognition
Algorithmic Pattern: Heap / Priority Queue (or Sorting)
Key Characteristics:
Need to find the "kth" element in some ordering
Don't need the entire sorted array, just a specific position
Trade-off between simple sorting vs. more efficient heap operations
"Largest" or "smallest" with a specific rank suggests heap usage
Similar Problems:
Kth Smallest Element in Array
Top K Frequent Elements
Find Median from Data Stream
Kth Largest Element in a Stream
Merge K Sorted Lists
2. High-Level Approach
Sorting Approach: Sort the array and directly access the kth largest element by indexing from the end.
Heap Approach: Convert to a max heap, pop k-1 times to remove larger elements, then the top of the heap is the kth largest. Since Python's heapq is a min-heap, negate all values to simulate a max heap.
3. Step-by-Step Logic
Sorting Approach:
Sort the array in ascending order
Why: After sorting, the kth largest is at a predictable position
Access element at index len(nums) - k
Why: In ascending order, the largest is at the end. Counting back k positions gives us the kth largest
Heap Approach:
Negate all numbers (multiply by -1)
Why: Python's heapq is a min-heap. Negating values makes smaller (more negative) numbers represent larger original values
Heapify the array to create a max heap structure
Why: This organizes data so we can efficiently extract the maximum element
Pop k-1 times from the heap
Why: Each pop removes the current maximum. After k-1 pops, the next element is the kth largest
Pop once more and negate to get the answer
Why: This is the kth largest element, but it's negative, so we restore the original value
4. Key Insights & Edge Cases
Key Insights:
The sorting approach is simpler and fine for most interviews, with O(n log n) time
The heap approach can be optimized further to O(n log k) using a min-heap of size k (not shown in your solution but worth knowing)
Critical: Do NOT remove duplicates with set() - duplicates count as separate positions in ranking
Implementation Gotchas:
Python's heapq only supports min-heap, so negate values for max-heap behavior
Remember to negate back when returning the final answer
heapify() modifies in-place and returns None, don't try to assign its result
Edge Cases:
Empty array (handled with your check)
k = 1 (should return maximum element)
k = len(nums) (should return minimum element)
All elements are the same
Array with duplicates (duplicates must be counted separately)
5. Pseudocode
Sorting Version:
function findKthLargest(nums, k):
    if nums is empty:
        return 0
    
    sort nums in ascending order
    return nums[length - k]

Heap Version:
function findKthLargest(nums, k):
    if nums is empty:
        return 0
    
    negate all elements in nums (to simulate max heap)
    convert nums to a heap structure
    
    repeat (k - 1) times:
        remove the top element from heap
    
    pop one more element and negate it
    return this value

6. Complexity Analysis
Sorting Approach:
Time Complexity: O(n log n)
Sorting dominates with O(n log n), array access is O(1)
Space Complexity: O(1) to O(n)
Depends on sorting algorithm; Python's Timsort uses O(n) space
Heap Approach (as implemented):
Time Complexity: O(n + k log n)
Heapify: O(n), then k pops of O(log n) each
If k is small, this approaches O(n)
If k is close to n, this is O(n log n)
Space Complexity: O(1)
In-place heap operations (modifies input array)
Note: An optimized heap approach using a min-heap of size k would be O(n log k) time, which is better when k << n.
"""
