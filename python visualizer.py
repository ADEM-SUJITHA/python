# Use memoization to optimize the recursive Fibonacci implementation.
fibonacci_cache = {}

def memoized_fibonacci(n):
    # Return 1 for the first and second Fibonacci numbers (base case)
    if n <= 2:
        return 1

    # If the result is already cached, return it from the cache
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Recursively calculate the Fibonacci number and store it in the cache
    fibonacci_cache[n] = memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
    return fibonacci_cache[n]

result = memoized_fibonacci(3)
print(result)