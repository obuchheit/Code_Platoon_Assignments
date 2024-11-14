def bubble_sort(lst:list[int])->list[int]:
    n = len(lst)
    for idx in range(n):
        for jdx in range(0, n - idx -1):
            if lst[jdx] > lst[jdx + 1]:
                lst[jdx], lst[jdx + 1] = lst[jdx + 1], lst[jdx]
    return lst 