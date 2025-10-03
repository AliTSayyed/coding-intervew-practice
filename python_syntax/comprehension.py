# List comprehension
arr = [i for i in range(5)]
print(arr)  # gives [0, 1, 2, 3, 4]


arr = [i + i for i in range(5)]
print(arr)  # gives [0, 2, 4, 3, 8]

# 2D lists
arr = [[0] * 4 for i in range(4)]  # dont even use i here
print(arr)  # this gives [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

# This won't work
arr = [[0] * 4] * 4
print(
    arr
)  # this will give the same output BUT if you modify one index it modifes all other indexes (they are treated like copies in this)

# Set comprehension
mySet = {i for i in range(5)}

# Dict comprehension
myMap = {
    i: 2 * i for i in range(3)
}  # most useful in graph problems such as building adjacency lists
