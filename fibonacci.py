def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memoization(n, cache={}):
    if cache.get(n, None):
        return cache.get(n)

    if n < 2:
        return n

    cache[n] = fibonacci_memoization(n - 1, cache) + fibonacci_memoization(n - 2, cache)
    return cache[n]


def fibonacci_iterative_dp(n):
    t = {}

    for i in range(n + 1):
        if i < 2:
            t[i] = i
        else:
            t[i] = t[i - 1] + t[i - 2]

    return t.get(n)


def fibonacci_iterative(n):
    if n < 2:
        return n

    n1 = 0
    n2 = 1
    r = None

    for i in range(2, n + 1):
        r = n1 + n2
        temp = n2
        n2 = r
        n1 = temp

    return r


print(fibonacci_iterative(8))
