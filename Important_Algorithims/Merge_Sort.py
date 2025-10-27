def merge_sort(arr):
    # Base case: arrays of length 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr

    # Divide: find the middle point
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Conquer: recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Combine: merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from left and right, add smaller to result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from left (if any)
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add remaining elements from right (if any)
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # [3, 9, 10, 27, 38, 43, 82]
