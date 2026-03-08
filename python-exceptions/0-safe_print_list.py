#!/usr/bin/python3
def safe_access(my_list, x):
    """Return element at index x if valid, else None."""
    try:
        return my_list[x]
    except IndexError:
        return None
