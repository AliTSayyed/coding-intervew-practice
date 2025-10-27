def quick_sort(input_array, low_index=0, high_index=None):
    # Handle default parameter for initial call
    if high_index is None:
        high_index = len(input_array) - 1

    # Recursion base case, exit if the range is 1 (i.e. indices are the same)
    # A sub array of 1 item is already sorted
    if low_index >= high_index:
        return

    # Make the pivot the value at the end of the subarray
    pivot = input_array[high_index]

    # Declare two pointers, one at the start of the array, the other just before
    # the pivot
    left_p = low_index
    right_p = high_index - 1

    # Move both pointers in towards each other
    # Pause the left pointer when it reaches a value greater than the pivot
    # Pause the right pointer when it reaches a value less than the pivot
    # At this point swap the values at the left and right pointers
    # Continue until left pointer is at the same spot as the right pointer
    while left_p < right_p:
        while input_array[left_p] <= pivot and left_p < right_p:
            left_p += 1
        while input_array[right_p] >= pivot and left_p < right_p:
            right_p -= 1
        swap(input_array, left_p, right_p)

    # After the loop, left_p == right_p at the partition point.
    # All elements to the left of left_p are ≤ pivot.
    # All elements to the right of left_p are ≥ pivot.
    # Swap the pivot into its correct final position.
    # The value at left_p when we break out must be ≥ pivot because otherwise the
    # left pointer would have continued moving
    # That's the whole point of the condition while (input_array[left_p] <= pivot).
    swap(input_array, left_p, high_index)

    # Recursively sort the sub array from low index to 1 index before the left
    # pointer (because the pivot value is now swapped there)
    quick_sort(input_array, low_index, left_p - 1)

    # Recursive sort the sub array from 1 past the left pointer (again pivot value
    # is there now), up to the high index
    quick_sort(input_array, left_p + 1, high_index)


def swap(input_array, index1, index2):
    temp = input_array[index1]
    input_array[index1] = input_array[index2]
    input_array[index2] = temp


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
quick_sort(arr)
print(arr)  # [3, 9, 10, 27, 38, 43, 82]

# Test with duplicates
arr2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quick_sort(arr2)
print(arr2)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
