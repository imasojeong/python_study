def quick_sort(A):
    def sort(lo, hi):
        if lo >= hi:
            return

        mid = partition(lo, hi)
        sort(lo, mid - 1)
        sort(mid + 1, hi)

    def partition(lo, hi):
        pivot = A[lo]  # 첫번째 원소를 pivot으로 삼음
        left = lo + 1
        right = hi

        while left <= right:
            while left <= hi and A[left] <= pivot:  # left <= pivot가 될 때까지 left 증가
                left += 1
            while A[right] >= pivot and right >= left:  # pivot <= hi가 될 때까지 right 감소
                right -= 1
            if right < left:
                break
            else:
                A[left], A[right] = A[right], A[left]

        A[lo], A[right] = A[right], A[lo]

        return right

    sort(0, len(A) - 1)

