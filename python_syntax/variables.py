# Variables are dynamically typed
n = 0
print('n = ', n)

n = 'abc'
print('n =',n)

# Multiple assignments (can use multiple types in the same line)
n, m = 0, "abc"

# Increment
n = n + 1 # good
n +=1 # better
# n++ not a thing

# None in null (absence of value)
n = 4
n = None
print("n = ", n)
