from collections import Counter
def frequency_flattened(nested_lists):
    """Flatten a list of lists and return a dict with element frequencies."""
    flat = [item for sublist in nested_lists for item in sublist]
    return dict(Counter(flat))
