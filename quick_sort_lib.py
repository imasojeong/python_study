def quick_sort(A):
    def sort(lo, hi):
        if lo >= hi: return  # 이미 정렬이 된 경우, 함수를 종료함
        mid = partition(lo, hi)
        sort(lo, mid - 1)
        sort(mid + 1, hi)

    def partition(lo, hi):
        pivot = A[lo]  # 첫번째 원소를 pivot으로 삼음
        while lo <= hi:
            while A[lo] < pivot:
                lo += 1
            while A[hi] > pivot:
                hi -= 1
            if lo <= hi:
                A[lo], A[hi] = A[hi], A[lo]
                lo, hi = lo + 1, hi - 1
        return lo

    return sort(0, len(A) - 1)