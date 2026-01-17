def QuickSort(a, lo, hi)
    def partition(lo, hi):
        pivot = a[hi]
        left =  lo
        for right in range(lo, hi):
            if a[right] < pivot:
                a[left], a[right] = a[right], a[left]
                left += 1
        a[left], a[hi] = a[hi], a[left]
        return left

    if lo < hi:
        pivot = partition(a, lo, hi)
        QuickSort(a, lo, pivot - 1)
        QuickSort(a, pivot, hi)

