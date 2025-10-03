# Division is decimal by default
print(5 / 2)  # this gives 2.5

# Double slash rounds down
print(5 // 2)  # this gives 2

# CAREFUL: most languages round towards 0 by
# default so negative numbers will round down
print(-3 // 2)  # this gives -2

# A workaround for rounding towards 0 is to
# use decimal devision and then convert to int
print(int(-3 / 2))  # this gives -1

# Modding is similar to most languages
print(10 % 3)  # this gives 1

# Except for negative values
print(-10 % 3)  # this gives -2

# to be consistent with other langauges modulo
import math

print(math.fmod(-10, 3))  # this gives -1.0

# More math helpers
print(math.floor(3.2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2, 3))

# Max / Min Int
float("inf")
float("-inf")

# Python numbers are infinite so they never over flow
print(math.pow(2, 200))

# But still less than infinity
print(math.pow(2, 200) < float("inf"))
