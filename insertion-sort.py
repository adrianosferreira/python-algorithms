def insertion_sort(l):
    for j in range(1, len(l)):
        k = l[j]
        i = j - 1

        while i >= 0 and l[i] > k:
            l[i + 1] = l[i]
            i -= 1

        l[i + 1] = k

    return l


print(insertion_sort([5, 4, 3, 2, 1]))
