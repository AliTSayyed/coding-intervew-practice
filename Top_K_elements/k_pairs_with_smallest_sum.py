"""
Problem:
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.


Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
"""

import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        # consider this like exploring a 2d matrix
        # the smallest value is at 0, 0. Values only increase going down and right
        visited = {(0, 0)}
        pq = []
        ret = []

        # start by adding 0,0 the smallest possible
        total = nums1[0] + nums2[0]
        heapq.heappush(pq, (total, 0, 0))

        # pop the smallest value and add the next two smallest (right and down)
        # do this until the ret len is the same as k
        while pq and len(ret) < k:
            total, i, j = heapq.heappop(pq)
            ret.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(pq, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

        return ret


"""
brute force
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = [] 
        stop = 0
      # create all possible pairs vs create pairs and push to heap 
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                total = nums1[i] + nums2[j]
                heapq.heappush(pairs, (total, (nums1[i],nums2[j]))) 
                stop += 1

      # return k items from heap
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(pairs)[1])
      # heap should store the min sums 

        return ret
"""

"""
1. Pattern Recognition
Pattern: Min-Heap with Lazy Evaluation / BFS on Virtual 2D Matrix
Key Characteristics:
Need k smallest elements from a large search space
Both input arrays are sorted
Can't afford to generate all combinations upfront
Want to explore candidates in increasing order
Similar Problems:
Kth Smallest Element in Sorted Matrix (LC 378)
Find K Pairs with Smallest Sums (this problem)
Merge K Sorted Lists (LC 23)
Smallest Range Covering Elements from K Lists (LC 632)
2. High-Level Approach
Treat the problem as exploring a virtual 2D matrix where matrix[i][j] = nums1[i] + nums2[j]. Since both arrays are sorted, this matrix has values increasing down and right. Start from the top-left (smallest sum) and use a min-heap to always extract the next smallest sum, exploring only the necessary adjacent cells (right and down) until k pairs are found.
3. Step-by-Step Logic
Initialize with smallest possible pair (0,0)


WHY: Since arrays are sorted, nums1[0] + nums2[0] is guaranteed to be the smallest sum
Pop the minimum sum from heap


WHY: Heap maintains all candidate pairs in sorted order by sum
Add current pair to result


WHY: The popped pair is the next smallest among all candidates
Explore adjacent positions: (i+1, j) and (i, j+1)


WHY: In a sorted matrix, the next potential smallest values can only be directly right or down from current position
Moving down: increment i (next element from nums1, same nums2 element)
Moving right: increment j (same nums1 element, next element from nums2)
Track visited positions to avoid duplicates


WHY: Position (i+1, j+1) can be reached from both (i+1, j) and (i, j+1), causing duplicates
Repeat until k pairs found or heap empty


WHY: Early termination once we have k pairs; heap empty handles k > total pairs
4. Key Insights & Edge Cases
What Makes This Work:
Sorted arrays create a "sorted matrix" property where values only increase right/down
Heap ensures we always process the globally smallest unprocessed sum
Lazy evaluation: only generate pairs as needed, not all n×m combinations
Important Details:
Must use a visited set - without it, you'll add duplicate positions to heap
Store indices (i, j) in heap, not just values, to track position
Heap tuple: (sum, i, j) - sum first for proper min-heap ordering
Edge Cases:
Empty arrays: return empty result
k larger than total possible pairs: loop terminates when heap is empty
k = 1: returns after first pop
Single element arrays: still works, only explores one direction
5. Pseudocode
function kSmallestPairs(nums1, nums2, k):
    if nums1 or nums2 is empty:
        return []
    
    heap = [(nums1[0] + nums2[0], 0, 0)]
    visited = {(0, 0)}
    result = []
    
    while heap is not empty AND result.length < k:
        (sum, i, j) = pop minimum from heap
        add [nums1[i], nums2[j]] to result
        
        // Explore down
        if i+1 is valid AND (i+1, j) not visited:
            push (nums1[i+1] + nums2[j], i+1, j) to heap
            mark (i+1, j) as visited
        
        // Explore right
        if j+1 is valid AND (i, j+1) not visited:
            push (nums1[i] + nums2[j+1], i, j+1) to heap
            mark (i, j+1) as visited
    
    return result

6. Complexity Analysis
Time Complexity: O(k log k)
We extract k elements from the heap
Each heap operation (push/pop) is O(log k) since heap size ≤ k
We add at most 2 new elements per pop, so heap never exceeds ~2k elements
Space Complexity: O(k)
Heap stores at most O(k) elements at any time
Visited set stores at most O(k) positions
Result array stores exactly k pairs
Comparison to Brute Force:
Brute Force: O(n×m log(n×m)) time, O(n×m) space
Optimized: O(k log k) time, O(k) space
Massive improvement when k << n×m

"""
