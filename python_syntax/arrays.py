# Arrays (called lists in python)
arr = [1, 2, 3]
print(arr)

# Can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

# can add many items to a list
arr.extend([7, 8, 9])

# list is not a stack so you can do inserts
arr.insert(1, 7)  # O(n) time insert operation
print(arr)

arr[0] = 0  # O(1) access / reassing operation

# Initilize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# Carful: -1 is not out of bounds,
# its the last value
arr = [1, 2, 3]
print(arr[-1])  # this gives 3

# Sublists (aka slicing)
# End value is not included
arr = [1, 2, 3, 4]
print(arr[1:3])  # this gives [2,3]

# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)  # gives 1 2 3,

# can be useful if you need to go through a list of pairs
pairs = [(1, 2), (3, 4), (5, 6)]
for x, y in pairs:
    print(f"x={x}, y={y}")

# be careful to have same number of vars as whats in the list
a, b = [1, 2, 3]  # will give error

# Pro tip: If you have extra values you want to ignore, you can use * notation
a, b, *rest = [1, 2, 3, 4, 5]  # a=1, b=2, rest=[3,4,5]
a, b, *_ = [1, 2, 3]  # a=1, b=2, ignore the rest

# Loop through arrays
nums = [1, 2, 3]

# Using index
for i in range(len(nums)):
    print(nums[i])

# Without index
for n in nums:
    print(n)

# With index and value
for i, n in enumerate(nums):
    print(i, n)

# Loop through multiple arrays simultaneously
# with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)  # (1, 2), (3, 4), (5, 6)

# Without zip (awkward):
for i in range(len(nums1)):
    print(nums1[i], nums2[i])

# With zip (clean):
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# can add lists
nums3 = [8, 9, 10]
nums3 += [11, 12, 13]
