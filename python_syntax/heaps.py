# Heaps
import heapq

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
