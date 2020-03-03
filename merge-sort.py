def merge_sort(l):
    if len(l) == 1:
        return l

    mid = int(len(l) / 2)
    left = l[0:mid]
    right = l[mid:len(l)]

    return merge(merge_sort(left), merge_sort(right))


def merge(l1, l2):
    res = []

    i = 0
    j = 0

    while i < len(l1) or j < len(l2):
        if j >= len(l2):
            res.append(l1[i])
            i += 1
        elif i >= len(l1):
            res.append(l2[j])
            j += 1
        elif l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1

    return res


print(merge_sort([1, 2, 10, 5, 20, 15, 12]))
