import random
import time
import merge_sort_lib
import quick_sort_lib
import heap_sort_lib

N = 40000
A = []

for i in range(N):
    num = random.randrange(1, N)
    A.append(num)

sorted_A = A.copy()  # 정확한 비교를 위하여 정렬 전 A를 복사해서 사용함

# Merge Sort
print("---Merge Sort---")
print("정렬 전 A :", sorted_A[0:5])
st = time.time()
merge_sort_lib.merge_sort(sorted_A)
et = time.time()
print("정렬 후 A : ", sorted_A[0:5])
print("Merge Sort Elapsed time=", (et-st))

sorted_A = A.copy()  # 정확한 비교를 위하여 정렬 전 A를 복사해서 사용함
# Quick Sort
print("---Quick Sort---")
print("정렬 전 A : ", sorted_A[0:5])
st = time.time()
quick_sort_lib.quick_sort(sorted_A)
et = time.time()
print("정렬 후 A : ", sorted_A[0:5])
print("Quick Sort Elapsed time=", (et-st))

sorted_A = A.copy()  # 정확한 비교를 위하여 정렬 전 A를 복사해서 사용함
# Heap Sort
print("---Heap Sort---")
print("정렬 전 A :", sorted_A[0:5])
st = time.time()
heap_sort_lib.heap_sort(sorted_A)
et = time.time()
print("정렬 후 A : ", sorted_A[0:5])
print("Heap Sort Elapsed time=", (et-st))
