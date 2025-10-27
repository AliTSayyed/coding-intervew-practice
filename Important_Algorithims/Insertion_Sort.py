def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Save the value to insert
        j = i - 1
        while j >= 0 and arr[j] > key:  # Check j >= 0 FIRST
            arr[j + 1] = arr[j]  # Shift element right
            j -= 1
        arr[j + 1] = key  # Insert the key in correct position
