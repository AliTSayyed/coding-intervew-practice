# Reverse O(n)
nums = [1, 2, 3]
nums.reverse()
print(nums)  # gives [3, 2, 1]

# Sorting O(nlogn)
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)

# Reverse sort
arr.sort(reverse=True)

# sorting strings
arr = ["bob", "alex", "joe", "alice"]
arr.sort()
print(arr)  # sorts in alphabetical order

# Custom sort (say by length of string)
# pass in a lambda function
# key expects a function that takes one argument (an element from the list)
# That function should return a value to sort by
arr.sort(key=lambda x: len(x))  # x is each element in the list

"""
lambda x: len(x)
  │    │    │
  │    │    └─── Return value (what the function produces)
  │    └──────── Parameter (input)
  └───────────── Keyword that says "this is an anonymous function"

  Equivilant to
  def some_function(x):
    return len(x)
"""
