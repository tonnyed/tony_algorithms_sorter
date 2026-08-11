"""Sorting algorithm implementations."""


def bubble_sort(data):
    """Return a sorted copy of data using Bubble Sort."""
    arr = data.copy()

    for i in range(len(arr)):
        swapped = False

        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Stop when the data is already sorted.
        if not swapped:
            break

    return arr


def heapify(arr, heap_size, root):
    """Restore the max-heap property."""
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, heap_size, largest)


def heap_sort(data):
    """Return a sorted copy of data using Heap Sort."""
    arr = data.copy()
    n = len(arr)

    # Build the max binary heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract the maximum element repeatedly.
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr