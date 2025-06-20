def count_divisors(n):
    """Return the number of divisors of integer n. n must be positive."""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 2 if i * i != n else 1
        i += 1
    return count
