# Heaps
import heapq

"""
Important Notes

Min-Heap Only: Python's heapq only implements min-heap. For max-heap, negate values.
Zero-Indexed: The smallest element is always at heap[0], but don't modify directly.
Use heap[0] to peek: Access the smallest element without removing it.
heapify() returns None: It modifies in-place, so heap = heapify(list) gives you None.
When to use what:

Need k largest/smallest? → Use nlargest() / nsmallest()
Building heap gradually? → Use heappush()
Converting existing list? → Use heapify()
Need both push and pop? → Use heappushpop() or heapreplace()
"""

# heaps are great for finding min and max of a set of values frequently
# under the hood heaps are just arrays maintianing values in the correct indecies
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 4)
heapq.heappush(minHeap, 3)

# Min is always at index 0
print(minHeap[0])

# how to loop through a heap
while len(minHeap):
    print(heapq.heappop(minHeap))

# Python does not have max heaps by default
# need to do a workaround
# use min heap and mulitply by -1 whenever you push & pop
maxHeap = []
heapq.heappush(maxHeap, -1 * 3)
heapq.heappush(maxHeap, -1 * 4)
heapq.heappush(maxHeap, -1 * 5)

# Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# Build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

heap = [3, 5, 7]
result = heapq.heappushpop(heap, 2)  # returns 2, heap becomes [3, 5, 7]

heap = [1, 3, 5]
result = heapq.heapreplace(heap, 4)  # returns 1, heap becomes [3, 4, 5]

nums = [5, 2, 8, 1, 9]
heapq.heapify(nums)  # nums becomes [1, 2, 8, 5, 9]

nums = [1, 8, 3, 2, 9, 5]
largest = heapq.nlargest(3, nums)  # returns [9, 8, 5]

# With key function
people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
oldest = heapq.nlargest(1, people, key=lambda x: x["age"])

nums = [1, 8, 3, 2, 9, 5]
smallest = heapq.nsmallest(3, nums)  # returns [1, 2, 3]

list1 = [1, 3, 5]
list2 = [2, 4, 6]
list3 = [0, 7, 8]
merged = list(heapq.merge(list1, list2, list3))  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
