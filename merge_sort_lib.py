def merge_sort(A):
    aux = [None] * len(A)

    def r_sort(lo, hi):
        if lo >= hi: return  # 이미 정렬이 된 경우, 함수를 종료함
        mid = (lo + hi) // 2
        r_sort(lo, mid)
        r_sort(mid + 1, hi)
        merge(lo, mid, hi)

    def merge(lo, mid, hi):
        aux[lo:hi + 1] = A[lo:hi + 1]
        left = lo
        right = mid + 1
        for i in range(lo, hi + 1):
            if left > mid:  # 왼쪽 부분 배열의 정렬이 완료된 경우, 오른쪽 부분 배열의 원소를 A에 추가함
                A[i] = aux[right]
                right += 1
            elif right > hi:  # 오른쪽 부분 배열의 정렬이 완료된 경우, 왼쪽 부분 배열의 원소를 A에 추가함
                A[i] = aux[left]
                left += 1
            elif aux[right] < aux[left]:  # 오른쪽 부분 배열의 현재 원소가 왼쪽 부분 배열의 현재 원소보다 작을 때, 오른쪽 부분 배열의 원소를 A에 추가함
                A[i] = aux[right]
                right += 1
            else:  # 왼쪽 부분 배열의 현재 원소가 오른쪽 부분 배열의 현재 원소보다 작거나 같을 때, 왼쪽 부분 배열의 원소를 A에 추가함
                A[i] = aux[left]
                left += 1

    r_sort(0, len(A) - 1)
