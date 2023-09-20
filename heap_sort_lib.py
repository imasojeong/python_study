def heapify(A, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and A[left_child] > A[largest]:
        largest = left_child

    if right_child < n and A[right_child] > A[largest]:
        largest = right_child

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)


def heap_sort(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)

