def binary_search(n, k):
    left = 0
    right = len(n) - 1

    while left <= right:
        mid = int(((right - left) / 2) + left)

        if n[mid] == k:
            return True

        if n[mid] > k:
            right = mid - 1
        else:
            left = mid + 1

    return False


print(binary_search([1, 4, 8, 9, 12, 20, 23, 25, 30, 50], 1))
