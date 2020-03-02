def bubble_sort(l):
    swapped = False
    for i in range(int(len(l)-1/2)):
        for j in range(len(l)-1):
            temp = l[j]
            if l[j] > l[j + 1]:
                l[j] = l[j + 1]
                l[j + 1] = temp

                swapped = True

        if swapped is False:
            return l
    return l


print(bubble_sort([1, 2, 3, 5, 4]))
