def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memoization(n, cache={}):
    if cache.get(n, None):
        return cache.get(n)

    if n < 2:
        return n

    cache[n] = fibonacci_memoization(n-1, cache) + fibonacci_memoization(n-2, cache)
    return cache[n]


def fibonacci_iterative(n):
    t = {}

    for i in range(n + 1):
        if i < 2:
            t[i] = i
        else:
            t[i] = t[i - 1] + t[i - 2]

    return t.get(n)

