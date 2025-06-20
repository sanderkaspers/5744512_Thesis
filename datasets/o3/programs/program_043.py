def min_list_length(lists):
    """Return the length of the shortest list in a list of lists."""
    if not lists:
        raise ValueError("lists must not be empty")
    return min(len(lst) for lst in lists)
