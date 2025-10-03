# Queues (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)  # right now this is similar to a list

queue.popleft()  # can remove from the left of the list (1 in this case)
print(queue)

queue.appendleft(1)  # can add from the left
print(queue)

queue.pop()  # can remove from right side
print(queue)

# can 'peek' via indexing to look up values
print(queue[-1])
print(queue[0])
