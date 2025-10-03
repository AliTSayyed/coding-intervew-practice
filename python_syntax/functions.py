# Functions
def myFunc(n, m):
    return n * m


print(myFunc(3, 4))


# Nested Functions have access to outer vairables
# Nested functions can be helpful in recursive problems
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c

    return inner()


# can be good in graph problems for keeping code concise
print(outer("a", "b"))


# Can modify objects be not reassing
# unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2

        # will only modify the val in the helper scope
        # val *= 2

        # this will modify val outside the helper scope
        nonlocal val
        val *= 2

    helper()
    print(arr, val)


nums = [1, 2]
val = 3
double(nums, val)
