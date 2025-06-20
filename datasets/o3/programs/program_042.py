def first_of_min_second(pairs):
    """Return the first element of the tuple that has the smallest second element."""
    if not pairs:
        raise ValueError("pairs must not be empty")
    return min(pairs, key=lambda t: t[1])[0]
