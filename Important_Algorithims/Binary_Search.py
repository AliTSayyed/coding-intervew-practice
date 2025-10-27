"""
Modified binary search refers to adapting the basic binary search algorithm to solve related problems, such as:

Finding first/last occurrence of a duplicate value
Finding insertion position for a value not in the array
Searching rotated sorted arrays (e.g., [4,5,6,7,0,1,2])
Finding peak elements in unsorted arrays
Search in 2D matrices
Finding square roots or other values using binary search on answer space

The core idea remains the same (divide and conquer), but you adjust the comparison logic and what you return based on the specific problem.
"""


# regular binary search assumes a sorted array
def BinarySearch(numbers: list[int], numberToFind: int) -> int:
    right = len(numbers) - 1
    left = 0

    # When the search narrows down to a single element, left and right both point to the same index.
    while left <= right:
        mid = (right + left) // 2

        value = numbers[mid]

        if value < numberToFind:
            left = mid + 1
        elif value > numberToFind:
            right = mid - 1
        else:
            return mid

    return -1


if __name__ == "__main__":
    list = [1, 3, 4, 5, 6, 7, 9, 10]
    numberToFind = 3

    print(f"{list}, Want {numberToFind}")

    found_index = BinarySearch(list, numberToFind)

    print(f"Number found at index: {found_index}")
