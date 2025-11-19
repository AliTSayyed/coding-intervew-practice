"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

import heapq


class Solution:
    def topKFrequent(self, nums, k: int):
        freq = {}
        # create a map with number and its frequency
        for i, value in enumerate(nums):
            freq[value] = freq.get(value, 0) + 1

        # create a heap and return the k largest items
        max_heap = []

        for number, count in freq.items():
            heapq.heappush(max_heap, (-count, number))

        ret = []
        for i in range(k):
            count, number = heapq.heappop(max_heap)
            ret.append(number)

        return ret


"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        # create a map with number and its frequency
        for i, value in enumerate(nums):
            freq[value] = freq.get(value, 0) + 1
        
        # create a heap and return the k largest items, we store the 
        return heapq.nlargest(k, freq.keys(), key=freq.get)

"""

"""
1. Pattern Recognition
Algorithmic Pattern: Hash Map + Heap (Priority Queue)
Key Characteristics:
Need to find "top K" elements based on some criteria (frequency, value, etc.)
Requires counting/tracking occurrences → Hash Map
Need to extract K elements in priority order → Heap
"Most/least frequent" or "top K" are strong heap indicators
Two-phase problem: aggregate data, then extract top results
Similar Problems:
Kth Largest Element in Array
Top K Frequent Words
Sort Characters by Frequency
K Closest Points to Origin
Find K Pairs with Smallest Sums
Reorganize String (uses frequency + heap)
2. High-Level Approach
Count the frequency of each unique number using a hash map. Build a max heap where elements are prioritized by their frequency (using negative counts since Python's heapq is a min-heap). Pop from the heap k times to extract the k most frequent elements.
3. Step-by-Step Logic
Build a frequency map


Why: We need to know how often each unique number appears before we can find the most frequent ones
Iterate through nums and count occurrences in a dictionary
Create a max heap with (negative_count, number) tuples


Why: We need to extract elements in order of highest frequency, but Python only has min-heap
Negate the counts to simulate max-heap behavior (smallest negative = largest positive)
Store tuples so we keep the number paired with its count
Push all (negative_count, number) pairs to the heap


Why: Heap organizes elements so we can efficiently extract the highest frequency items
Tuples are compared by first element (the negative count), giving us frequency-based ordering
Pop k times from the heap


Why: Each pop gives us the next most frequent element
Extract just the number from the tuple (ignore the count in results)
Return the list of k numbers


Why: These are the k numbers with the highest frequencies
4. Key Insights & Edge Cases
Key Insights:
Tuple ordering: Heaps compare tuples element-by-element, so (-count, num) sorts primarily by count
Why tuples? Can't just push counts alone—you'd lose track of which number has that count
Negation trick: -count converts min-heap to max-heap behavior
Alternative: Could use heapq.nlargest(k, freq.keys(), key=freq.get) for cleaner code
Implementation Gotchas:
Must negate counts for max-heap behavior
Don't forget to extract just the number from the tuple when building results
If two numbers have the same frequency, heap breaks ties by the second element (the number itself)
Edge Cases:
k equals the number of unique elements (return all unique numbers)
All numbers have the same frequency (any k numbers are valid)
k = 1 (find single most frequent element)
Array with single unique element repeated
Array where all elements are unique (frequency = 1 for all)
5. Pseudocode
function topKFrequent(nums, k):
    // Phase 1: Count frequencies
    create empty hash map freq
    for each number in nums:
        increment freq[number]
    
    // Phase 2: Build max heap
    create empty max_heap
    for each (number, count) in freq:
        push (-count, number) to max_heap
    
    // Phase 3: Extract top k
    create empty result list
    repeat k times:
        pop (neg_count, number) from max_heap
        add number to result
    
    return result

6. Complexity Analysis
Time Complexity: O(n + m log m)
O(n) to build frequency map (iterate through all n elements)
O(m log m) to build heap, where m = number of unique elements (push m items, each push is O(log m))
O(k log m) to pop k times from heap
Total: O(n + m log m + k log m) = O(n + m log m) since k ≤ m
Space Complexity: O(m)
O(m) for the frequency hash map (m unique elements)
O(m) for the heap (storing all m unique elements)
O(k) for the result array
Total: O(m) where m ≤ n
Note: There's an O(n) average time solution using Bucket Sort or Quickselect, but the heap approach is more intuitive and sufficient for interviews.
"""
